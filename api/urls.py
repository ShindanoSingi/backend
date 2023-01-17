from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .viewSets import UserViewSet, ProductViewSet, ExpenseViewSet, RevenueViewSet, BodabodaViewSet, ExpenseBodabodaViewSet, RevenueBodabodaViewSet, ExpenseProductViewSet, RevenueProductViewSet, TodoViewSet, TodoUserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet),

router.register('todos', TodoViewSet),

router.register('todousers', TodoUserViewSet),

router.register('revenues', RevenueViewSet),
router.register('expenses', ExpenseViewSet),

router.register('products', ProductViewSet),
router.register('expenseProduct', ExpenseProductViewSet),
router.register('revenueProduct', RevenueProductViewSet),

router.register('bodaboda', BodabodaViewSet),
router.register('revenuesbodaboda', RevenueBodabodaViewSet),
router.register('expensesbodaboda', ExpenseBodabodaViewSet),

urlpatterns = [
    path('', include(router.urls)),
]