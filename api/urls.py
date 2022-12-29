from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, ProductViewSet, ExpenseViewSet, RevenueViewSet, BodabodaViewSet, ExpenseBodabodaViewSet, RevenueBodabodaViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('products', ProductViewSet)
router.register('revenues', RevenueViewSet)
router.register('expenses', ExpenseViewSet)
router.register('bodaboda', BodabodaViewSet)
router.register('revenuesbodaboda', RevenueBodabodaViewSet)
router.register('expensesbodaboda', ExpenseBodabodaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
