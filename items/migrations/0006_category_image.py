# Generated by Django 3.0.2 on 2020-03-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default='', max_length=500),
        ),
    ]
