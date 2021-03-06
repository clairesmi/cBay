# Generated by Django 3.0.2 on 2020-03-05 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_buyer'),
        ('jwt_auth', '0012_auto_20200305_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='items_listed',
        ),
        migrations.AddField(
            model_name='listing',
            name='listed_items',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='items.Item'),
        ),
        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='listings', to=settings.AUTH_USER_MODEL),
        ),
    ]
