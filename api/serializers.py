from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Product, ExpenseProduct, RevenueProduct, Expense, Revenue, Bodaboda, ExpenseBodaboda, RevenueBodaboda, Todo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'item', 'price', 'image', 'countryOfOrigin']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'item', 'price', 'date_created']


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = ['id', 'item', 'price', 'date_created']

class ExpenseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseProduct
        fields = ['id', 'item', 'price', 'date_created']


class RevenueProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueProduct
        fields = ['id', 'item', 'price', 'date_created']


class BodabodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodaboda
        fields = ['id', 'item', 'price']


class ExpenseBodabodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseBodaboda
        fields = ['id', 'item', 'price', 'date_created']


class RevenueBodabodaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueBodaboda
        fields = ['id', 'item', 'price', 'date_created']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'todo', 'completed', 'date_created']

    def add_fields(self, instance):
        data = super().add_fields(instance)
        data['task_completed'] = instance.task_completed()
        return data
