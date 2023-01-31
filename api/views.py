from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import logout
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProductSerializer, ExpenseSerializer, RevenueSerializer, BodabodaSerializer, ExpenseBodabodaSerializer, RevenueBodabodaSerializer, ExpenseProductSerializer, RevenueProductSerializer, TodoSerializer, TodoUserSerializer
from .models import Product, Expense, Revenue, Bodaboda, ExpenseBodaboda, RevenueBodaboda, ExpenseProduct, RevenueProduct, Todo, TodoUser
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class LogoutViewSet(viewsets.ViewSet):
    def logout_user(self, request):
        logout(request)
        return
        Response(status=status.HTTP_204_NO_CONTENT)

# Get all users
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create a user
class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Delete a user
class UserDestroy(DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    serializer_class = UserSerializer


# Get all products
class ProductList(ListAPIView):
    queryset = Product.objects.all().order_by('countryOfOrigin','item')
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Create a product
class ProductCreate(CreateAPIView):
    queryset = Product.objects.all().order_by('countryOfOrigin','item')
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Update a product
class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Destroy a product
class ProductDestroy(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# ________________________________________________________________________________________________________________

# Get all expenses
class ExpenseList(ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Create an expense
class ExpenseCreate(CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Update an expense
class ExpenseUpdate(UpdateAPIView):
    queryset = Expense.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Destroy an expense
class ExpenseDestroy(DestroyAPIView):
    queryset = Expense.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# ________________________________________________________________________________________________________________

# Get all revenues
class RevenueList(ListAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Create a revenue
class RevenueCreate(CreateAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Update a revenue
class RevenueUpdate(UpdateAPIView):
    queryset = Revenue.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# Destroy a revenue
class RevenueDestroy(DestroyAPIView):
    queryset = Revenue.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueSerializer
    authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]

# ________________________________________________________________________________________________________________

# Get all bodaboda
class BodabodaList(ListAPIView):
    queryset = Bodaboda.objects.all()
    serializer_class = BodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a bodaboda
class BodabodaCreate(CreateAPIView):
    queryset = Bodaboda.objects.all()
    serializer_class = BodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a bodaboda
class BodabodaUpdate(UpdateAPIView):
    queryset = Bodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = BodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a bodaboda
class BodabodaDestroy(DestroyAPIView):
    queryset = Bodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = BodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# ________________________________________________________________________________________________________________

# Get all bodaboda Expenses
class ExpenseBodabodaList(ListAPIView):
    queryset = ExpenseBodaboda.objects.all()
    serializer_class = ExpenseBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a bodaboda expense
class ExpenseBodabodaCreate(CreateAPIView):
    queryset = ExpenseBodaboda.objects.all()
    serializer_class = ExpenseBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a bodaboda expense
class ExpenseBodabodaUpdate(UpdateAPIView):
    queryset = ExpenseBodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a bodaboda expense
class ExpenseBodabodaDestroy(DestroyAPIView):
    queryset = ExpenseBodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# ________________________________________________________________________________________________________________

# Get all bodaboda revenues
class RevenueBodabodaList(ListAPIView):
    queryset = RevenueBodaboda.objects.all()
    serializer_class = RevenueBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a bodaboda revenue
class RevenueBodabodaCreate(CreateAPIView):
    queryset = RevenueBodaboda.objects.all()
    serializer_class = RevenueBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a bodaboda revenue
class RevenueBodabodaUpdate(UpdateAPIView):
    queryset = RevenueBodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a bodaboda revenue
class RevenueBodabodaDestroy(DestroyAPIView):
    queryset = RevenueBodaboda.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueBodabodaSerializer
    authentication_classes = [TokenAuthentication, ]

# ________________________________________________________________________________________________________________

# Get all produts expenses
class ExpenseProductList(ListAPIView):
    queryset = ExpenseProduct.objects.all()
    serializer_class = ExpenseProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a product expense
class ExpenseProductCreate(CreateAPIView):
    queryset = ExpenseProduct.objects.all()
    serializer_class = ExpenseProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a product expense
class ExpenseProductUpdate(UpdateAPIView):
    queryset = ExpenseProduct.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a product expense
class ExpenseProductDestroy(DestroyAPIView):
    queryset = ExpenseProduct.objects.all()
    lookup_field = 'id'
    serializer_class = ExpenseProductSerializer
    authentication_classes = [TokenAuthentication, ]

# ________________________________________________________________________________________________________________

# Get all produts revenues
class RevenueProductList(ListAPIView):
    queryset = RevenueProduct.objects.all()
    serializer_class = RevenueProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a product revenue
class RevenueProductCreate(CreateAPIView):
    queryset = RevenueProduct.objects.all()
    serializer_class = RevenueProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a product revenue
class RevenueProductUpdate(UpdateAPIView):
    queryset = RevenueProduct.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueProductSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a product revenue
class RevenueProductDestroy(DestroyAPIView):
    queryset = RevenueProduct.objects.all()
    lookup_field = 'id'
    serializer_class = RevenueProductSerializer
    authentication_classes = [TokenAuthentication, ]


# Get all todos
class TodoList(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]


# Create a todo
class TodoCreate(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a todo
class TodoUpdate(UpdateAPIView):
    queryset = Todo.objects.all()
    lookup_field = 'id'
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a todo
class TodoDestroy(DestroyAPIView):
    queryset = Todo.objects.all()
    lookup_field = 'id'
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]



# Get all todos
class TodoUserList(ListAPIView):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer
    authentication_classes = [TokenAuthentication, ]

# Create a todo
class TodoUserCreate(CreateAPIView):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserSerializer
    authentication_classes = [TokenAuthentication, ]

# Update a todo
class TodoUserUpdate(UpdateAPIView):
    queryset = TodoUser.objects.all()
    lookup_field = 'id'
    serializer_class = TodoUserSerializer
    authentication_classes = [TokenAuthentication, ]

# Destroy a todo
class TodoUserDestroy(DestroyAPIView):
    queryset = TodoUser.objects.all()
    lookup_field = 'id'
    serializer_class = TodoUserSerializer
    authentication_classes = [TokenAuthentication, ]
