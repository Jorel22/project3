# Generated by Django 2.0.3 on 2019-12-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_delete_confirmed_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmed_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('total', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]