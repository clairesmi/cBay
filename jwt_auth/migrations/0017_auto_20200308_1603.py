# Generated by Django 3.0.2 on 2020-03-08 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_buyer'),
        ('jwt_auth', '0016_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='listed_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='listings', to='items.Item'),
        ),
    ]
