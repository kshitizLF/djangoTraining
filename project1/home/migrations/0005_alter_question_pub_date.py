# Generated by Django 5.0.1 on 2024-01-16 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_member_age_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.date(2024, 1, 16)),
        ),
    ]
