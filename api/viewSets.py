from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProductSerializer, ExpenseSerializer, RevenueSerializer, BodabodaSerializer, ExpenseBodabodaSerializer, RevenueBodabodaSerializer, ExpenseProductSerializer, RevenueProductSerializer, TodoSerializer, TodoUserSerializer
from .models import Product, Expense, Revenue, Bodaboda, ExpenseBodaboda, RevenueBodaboda, ExpenseProduct, RevenueProduct, Todo, TodoUser



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all();
    serializer_class = UserSerializer;

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('countryOfOrigin', 'item');
    serializer_class = ProductSerializer;
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all();
    serializer_class = ExpenseSerializer;
    authentication_classes = [TokenAuthentication, ];
    # permission_classes = [IsAuthenticated, ]

class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all();
    serializer_class = RevenueSerializer;
    authentication_classes = [TokenAuthentication, ];
    # permission_classes = [IsAuthenticated, ]

class BodabodaViewSet(viewsets.ModelViewSet):
    queryset = Bodaboda.objects.all();
    serializer_class = BodabodaSerializer;
    authentication_classes = [TokenAuthentication, ];
    # permission_classes = [IsAuthenticated, ]

class ExpenseBodabodaViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBodaboda.objects.all();
    serializer_class = ExpenseBodabodaSerializer;
    authentication_classes = [TokenAuthentication, ];
    # permission_classes = [IsAuthenticated, ]

class RevenueBodabodaViewSet(viewsets.ModelViewSet):
    queryset = RevenueBodaboda.objects.all()
    serializer_class = RevenueBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class ExpenseProductViewSet (viewsets.ModelViewSet):
    queryset = ExpenseProduct.objects.all()
    serializer_class = ExpenseProductSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class RevenueProductViewSet(viewsets.ModelViewSet):
    queryset = RevenueProduct.objects.all()
    serializer_class = RevenueProductSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

class TodoUserViewSet(viewsets.ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
