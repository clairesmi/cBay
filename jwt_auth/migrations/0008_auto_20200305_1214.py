# Generated by Django 3.0.2 on 2020-03-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0007_user_items_listed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='items_listed',
            field=models.CharField(default='', max_length=50),
        ),
    ]
