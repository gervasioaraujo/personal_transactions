from django.urls import include, path
from rest_framework import routers
# from .views import TransactionViewSet
from .views import TransactionCreate, TransactionList, TransactionUpdate, TransactionDelete


# router = routers.DefaultRouter()
# router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('', TransactionList.as_view()),
    path('create', TransactionCreate.as_view()),
    path('<int:pk>/update', TransactionUpdate.as_view()),
    path('<int:pk>/delete', TransactionDelete.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
