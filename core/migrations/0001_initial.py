# Generated by Django 4.2 on 2023-12-15 16:41

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='123', length=5, max_length=20, prefix='AE-', unique=True)),
                ('title', models.CharField(default='Lodge', max_length=100)),
            ],
        ),
    ]
