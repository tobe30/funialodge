# Generated by Django 4.2 on 2023-12-18 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_lodges_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lodges',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='lodges',
            name='longitude',
        ),
    ]