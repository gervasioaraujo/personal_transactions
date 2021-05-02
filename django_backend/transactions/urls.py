from django.urls import include, path
from rest_framework import routers

from .views import TransactionListCreateView, TransactionRetrieveUpdateDestroyView
# TransactionCreate, TransactionList, TransactionUpdate, TransactionDelete


urlpatterns = [
    path('', TransactionListCreateView.as_view()),
    path('<int:id>', TransactionRetrieveUpdateDestroyView.as_view()),
    # path('', TransactionList.as_view()),
    # path('create', TransactionCreate.as_view()),
    # path('<int:pk>/update', TransactionUpdate.as_view()),
    # path('<int:pk>/delete', TransactionDelete.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
