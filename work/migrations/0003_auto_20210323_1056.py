# Generated by Django 3.1.7 on 2021-03-23 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_remove_indent_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='week',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='weekno',
        ),
    ]
