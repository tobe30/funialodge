from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User



# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=5, max_length=20, prefix="AE-", alphabet="123")
    title = models.CharField(max_length=100, default="Lodge")

    class meta:
        verbose_name_plural = "Categories"

    
    def __str__(self):
        return self.title
    
class Lodges(models.Model):
    lid = ShortUUIDField(unique=True, length=5, max_length=20,  alphabet="ae123")
    title = models.CharField(max_length=100, default="Name of lodge")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    price = models.DecimalField(max_digits=99999999999999, decimal_places=0, default="0.00")
    description = models.TextField(blank=True, null=True)
    rooms = models.IntegerField(default=0)
    floor = models.IntegerField(default=0)
    available =models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
    

    class meta:
        verbose_name_plural = "Lodges"

    def lodge_Image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-mages", default="product.jpg")
    lodge = models.ForeignKey(Lodges, related_name="p_image", on_delete=models.SET_NULL, null=True)
    date  =  models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Lodge Images"


