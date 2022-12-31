# Generated by Django 4.1.3 on 2022-12-30 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_remove_todo_todo_user_todouser_todo"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todouser",
            name="todo",
        ),
        migrations.AddField(
            model_name="todo",
            name="todo_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.todouser",
            ),
        ),
    ]
