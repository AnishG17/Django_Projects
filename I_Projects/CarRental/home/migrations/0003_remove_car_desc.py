# Generated by Django 3.1.7 on 2021-08-13 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_customer_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='desc',
        ),
    ]