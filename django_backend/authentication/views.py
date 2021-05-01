from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.contrib import auth
from django.contrib.auth.models import User
import jwt
from django.conf import settings

from .serializers import UserSerializer


class UserRegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserRegisterView(generics.GenericAPIView):

#     serializer_class = UserSerializer

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.GenericAPIView):

    #####
    # serializer_class = UserSerializer

    def post(self, request):
        data = request.data

        username = data.get('username', None)
        password = data.get('password', None)
        # email = data.get('email', None)

        #####
        user = auth.authenticate(username=username, password=password)
        # user = User.objects.get(username=username, password=password)

        print(user)

        if user:

            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
