# Generated by Django 4.2 on 2023-12-16 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_lodges_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodges',
            name='floor',
            field=models.IntegerField(default=0),
        ),
    ]
