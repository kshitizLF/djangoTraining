# Generated by Django 5.0.1 on 2024-01-19 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_armyman_civilian'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArmyMan',
        ),
        migrations.DeleteModel(
            name='Civilian',
        ),
    ]
