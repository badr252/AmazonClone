# Generated by Django 4.2 on 2023-09-27 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_alter_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 16, 49, 23, 690271, tzinfo=datetime.timezone.utc), verbose_name='Created_at'),
        ),
    ]
