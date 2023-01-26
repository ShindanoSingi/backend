from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register('users', UserViewSet)
# router.register('products', ProductViewSet)
# router.register('revenues', RevenueViewSet)
# router.register('expenses', ExpenseViewSet)
# router.register('bodaboda', BodabodaViewSet)
# router.register('revenuesbodaboda', RevenueBodabodaViewSet)
# router.register('expensesbodaboda', ExpenseBodabodaViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', include(router.urls)),

    path('users/', views.UserList.as_view()),
    path('users/create/', views.UserCreate.as_view()),
    path('users/delete/<int:id>', views.UserDestroy.as_view()),

    path('products/', views.ProductList.as_view()),
    path('products/create', views.ProductCreate.as_view()),
    path('products/update/<int:int>', views.ProductUpdate.as_view()),
    path('products/delete/<int:id>', views.ProductDestroy.as_view()),

    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/create', views.ExpenseCreate.as_view()),
    path('expenses/update/<int:id>', views.ExpenseUpdate.as_view()),
    path('expenses/delete/<int:id>', views.ExpenseDestroy.as_view()),

    path('revenues/', views.RevenueList.as_view()),
    path('revenues/create', views.RevenueCreate.as_view()),
    path('revenues/update/<int:id>', views.RevenueUpdate.as_view()),
    path('revenues/delete/<int:id>', views.RevenueDestroy.as_view()),

    path('bodabodas/', views.BodabodaList.as_view()),
    path('bodabodas/create', views.BodabodaCreate.as_view()),
    path('bodabodas/update/<int:id>', views.BodabodaUpdate.as_view()),
    path('bodabodas/delete/<int:id>', views.BodabodaDestroy.as_view()),

    path('bodabodaExpenses/', views.ExpenseBodabodaList.as_view()),
    path('bodabodaExpenses/create', views.ExpenseBodabodaCreate.as_view()),
    path('bodabodaExpenses/update/<int:id>', views.ExpenseBodabodaUpdate.as_view()),
    path('bodabodaExpenses/delete/<int:id>', views.ExpenseBodabodaDestroy.as_view()),

    path('bodabodaRevenues/', views.RevenueBodabodaList.as_view()),
    path('bodabodaExpenses/create', views.RevenueBodabodaCreate.as_view()),
    path('bodabodaExpenses/update/<int:id>', views.RevenueBodabodaUpdate.as_view()),
    path('bodabodaExpenses/delete/<int:id>', views.RevenueBodabodaDestroy.as_view()),

    path('productsExpenses/', views.ExpenseProductList.as_view()),
    path('productsExpenses/create', views.ExpenseProductCreate.as_view()),
    path('productsExpenses/update/<int:id>', views.ExpenseProductUpdate.as_view()),
    path('productsExpenses/delete/<int:id>', views.ExpenseProductDestroy.as_view()),

    path('productsRevenues/', views.RevenueProductList.as_view()),
    path('productsRevenues/create', views.RevenueProductCreate.as_view()),
    path('productsRevenues/update/<int:id>', views.RevenueProductUpdate.as_view()),
    path('productsRevenues/delete/<int:id>', views.RevenueProductDestroy.as_view()),

    path('todos/', views.TodoList.as_view()),
    path('todos/create', views.TodoCreate.as_view()),
    path('todos/update/<int:id>', views.TodoUpdate.as_view()),
    path('todos/delete/<int:id>', views.TodoDestroy.as_view()),
]
