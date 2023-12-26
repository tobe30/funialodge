from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, ProductImagesForm
from core.models import  Lodges
from django.contrib import messages
from userauths.models import Profile, ContactUs
from userauths.forms import  ProfileForm
# Create your views here.
@login_required
def index(request):

    product = Lodges.objects.filter(user=request.user)

    context = {
        'product': product,
    }

    return render(request, 'dashboard/index.html', context)

def new(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        image_form = ProductImagesForm(request.POST, request.FILES)

        if form.is_valid():
            lodge = form.save(commit=False)
            lodge.user = request.user
            lodge.save()
            
            image = image_form.save(commit=False)
            image.lodge = lodge
            image.save()
            messages.success(request, f"Added succefully")

            return redirect('dashboard:lodges')
    else:
         form = NewItemForm()
         image_form = ProductImagesForm()

    return render(request, "dashboard/add-lodge.html", {
        'form':form,
        
    })
@login_required
def Contact(request):

    product = ContactUs.objects.filter(user=request.user)

    context = {
        'product': product,
    }
    return render(request, "dashboard/contact.html", context)

def lodge(request):

    product = Lodges.objects.filter(user=request.user)

    context = {
        'product': product,
    }
    return render(request, "dashboard/lodges.html", context)

def delete_product(request, lid):
    product = Lodges.objects.get(lid=lid)
    product.delete()
    messages.success(request, f"Deleted Successfully.")
    return redirect("dashboard:lodges")

@login_required
def dashboard_edit(request, lid):
    product = Lodges.objects.get(lid=lid, user=request.user)

    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            form.save_m2m()
            messages.success(request, f"edited succefully")

        return redirect("dashboard:lodges")
    else:
        form = NewItemForm(instance=product)
    context = {
        'form':form,
        'product':product,
    }
    return render(request, "dashboard/edit-lodge.html", context)
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    context = {
        "profile":profile
    }

    return render(request, "dashboard/user-profile.html", context)
@login_required
def edit_profile(request):

    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, "Profile Updated Successfully.")
            return redirect("dashboard:profile")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
    }

    return render(request, "dashboard/edit-profile.html", context)


