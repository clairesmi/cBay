# Generated by Django 3.0.2 on 2020-01-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_item_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(default='', max_length=50),
        ),
    ]
