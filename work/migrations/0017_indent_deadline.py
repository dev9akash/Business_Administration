# Generated by Django 3.1.7 on 2021-03-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_paymentfollow_total_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='indent',
            name='deadline',
            field=models.CharField(default='', max_length=30),
        ),
    ]