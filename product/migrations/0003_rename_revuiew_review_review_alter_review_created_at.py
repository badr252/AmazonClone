# Generated by Django 4.2 on 2023-08-29 22:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_tags_alter_review_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='revuiew',
            new_name='review',
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 22, 44, 10, 175561, tzinfo=datetime.timezone.utc), verbose_name='Created_at'),
        ),
    ]
