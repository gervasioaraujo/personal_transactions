from rest_framework import serializers

from .models import Transaction

# class TransactionSerializer(serializers.HyperlinkedModelSerializer):


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ['pk', 'operation_type', 'description', 'amount']
