# Generated by Django 3.0.2 on 2020-03-08 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0020_user_listed_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='listed_item',
        ),
    ]
