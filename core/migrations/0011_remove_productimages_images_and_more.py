# Generated by Django 4.2 on 2023-12-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_productimagegallery_alter_productimages_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimages',
            name='images',
        ),
        migrations.DeleteModel(
            name='ProductImageGallery',
        ),
        migrations.AddField(
            model_name='productimages',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='product-mages'),
        ),
    ]
