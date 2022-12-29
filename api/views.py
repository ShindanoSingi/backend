from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProductSerializer, ExpenseSerializer, RevenueSerializer, BodabodaSerializer, ExpenseBodabodaSerializer, RevenueBodabodaSerializer
from .models import Product, Expense, Revenue, Bodaboda, ExpenseBodaboda, RevenueBodaboda, ExpenseProduct, RevenueProduct, Todo


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]


class BodabodaViewSet(viewsets.ModelViewSet):
    queryset = Bodaboda.objects.all()
    serializer_class = BodabodaSerializer


class ExpenseBodabodaViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBodaboda.objects.all()
    serializer_class = ExpenseBodabodaSerializer


class RevenueBodabodaViewSet(viewsets.ModelViewSet):
    queryset = RevenueBodaboda.objects.all()
    serializer_class = RevenueBodabodaSerializer
