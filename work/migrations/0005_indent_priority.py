# Generated by Django 3.1.7 on 2021-03-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_auto_20210323_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='indent',
            name='priority',
            field=models.CharField(default='0000000', editable=False, max_length=10),
        ),
    ]
