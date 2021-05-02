from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import TransactionSerializer
from .models import Transaction


# class TransactionViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows transactions to be viewed or edited.
#     """
#     queryset = Transaction.objects.all().order_by('-created_at')
#     serializer_class = TransactionSerializer
#     # permission_classes = [permissions.IsAuthenticated]


class TransactionListCreateView(generics.ListCreateAPIView):

    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user).order_by('-created_at')


class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field="id"
    
    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


# class TransactionCreate(generics.CreateAPIView):

#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


# class TransactionList(generics.ListAPIView):

#     queryset = Transaction.objects.all().order_by('-created_at')
#     serializer_class = TransactionSerializer
#     # permission_classes = [permissions.IsAuthenticated]


# class TransactionUpdate(generics.RetrieveUpdateAPIView):

#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer


# class TransactionDelete(generics.DestroyAPIView):

#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
