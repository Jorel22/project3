# Generated by Django 2.0.3 on 2019-12-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_confirmed_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmed_order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
