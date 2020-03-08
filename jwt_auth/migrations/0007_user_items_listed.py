# Generated by Django 3.0.2 on 2020-03-05 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_item_buyer'),
        ('jwt_auth', '0006_auto_20200302_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='items_listed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='items.Item'),
        ),
    ]
