from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):

    INCOME = 'INCOME'
    EXPENSE = 'EXPENSE'
    TRANSACTION_TYPE_CHOICES = [
        (INCOME, 'Receita'),
        (EXPENSE, 'Despesa'),
    ]

    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    operation_type = models.CharField(
        max_length=20, choices=TRANSACTION_TYPE_CHOICES)
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        operation_type = 'Receita' if self.operation_type == self.INCOME else 'Despesa'
        return "R$ {} ({})".format(self.amount, operation_type)

    class Meta:
        verbose_name = 'transação'
        verbose_name_plural = "transações"
