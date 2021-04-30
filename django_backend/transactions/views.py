from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from .serializers import TransactionSerializer
from .models import Transaction


# class TransactionViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows transactions to be viewed or edited.
#     """
#     queryset = Transaction.objects.all().order_by('-created_at')
#     serializer_class = TransactionSerializer
#     # permission_classes = [permissions.IsAuthenticated]

class TransactionCreate(generics.CreateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionList(generics.ListAPIView):

    queryset = Transaction.objects.all().order_by('-created_at')
    serializer_class = TransactionSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TransactionUpdate(generics.RetrieveUpdateAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDelete(generics.DestroyAPIView):

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
