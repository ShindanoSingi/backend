from django.contrib import admin
from .models import Revenue, Product, Expense, Bodaboda, ExpenseBodaboda, RevenueBodaboda, ExpenseProduct, RevenueProduct, Todo, TodoUser

# Register your models here.
admin.site.register(ExpenseProduct)
admin.site.register(RevenueProduct)
admin.site.register(Todo)
admin.site.register(TodoUser)
admin.site.register(Product)
admin.site.register(Expense)
admin.site.register(Revenue)
admin.site.register(Bodaboda)
admin.site.register(ExpenseBodaboda)
admin.site.register(RevenueBodaboda)
