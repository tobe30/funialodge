# Generated by Django 4.2 on 2023-12-18 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_lodges_latitude_lodges_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodges',
            name='updated',
        ),
    ]