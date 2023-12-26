from core.models import Lodges, ProductImages
from django import forms


class NewItemForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Name of Lodge", "class":"form-control"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': "Lodge Description", "class":"form-control"}))
    price = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': "Sale Price", "class":"form-control"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    rooms = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Number of rooms", "class":"form-control"}))
    floor = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Number of floors", "class":"form-control"}))
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={"class":"form-control", "multiple": True}))
    class Meta:
        model = Lodges
        fields = [
            'title',
            'image',
            'description',
            'price',
            'rooms',
            'floor',
            'category',
            'images'
        ]

class ProductImagesForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['images']
   