# Generated by Django 3.0.2 on 2020-03-02 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jwt_auth', '0003_recommendations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recommendations',
            new_name='Recommendation',
        ),
    ]
