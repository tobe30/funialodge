from django.shortcuts import render, get_object_or_404, redirect
from core.models import Lodges, Category
from userauths.models import Profile, User, ContactUs
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.
def email(request):
    return render(request, "core/email.html")

def index(request):

    lodge = Lodges.objects.filter(available=True)[0:3]

    context = {
        "lodge":lodge
    }

    if request.method == 'POST':
        
        form = ContactUs(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            message=request.POST['message'],
            user=request.user
        )
        form.save()
        messages.success(request, "Message sent Successfully.")
        return redirect("core:index")
    else:
       

        return render(request, 'core/index.html', context)

def lodges(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    lodge = Lodges.objects.filter(available=True).order_by("-id")

    if category_id:
        lodge = lodge.filter(category_id=category_id)

    if query:
        lodge = lodge.filter(Q(title__icontains=query) | Q(description__icontains=query))

    context ={
        "lodge":lodge,
        'query':query,
        'categories':categories,
        'category_id': int(category_id)
    }

    return render(request, 'core/lodges.html', context)

def details(request, lid):

    lodge = Lodges.objects.get(lid=lid)
    user = User.objects.all()
    
    #product = get_object_or_404(Product, lid=lid)

    p_image = lodge.p_image.all()

    context ={
        "lodge":lodge,
        "p_image":p_image,
        "user":user
    }

    return render(request, 'core/details.html', context)


def filter_product(request):
   
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']

    products = Lodges.objects.filter(available=True).order_by("-id").distinct()

    products = products.filter(price__gte=min_price)
    products = products.filter(price__lte=max_price)

    
    data = render_to_string("core/async/lodges.html", {"products": products})
    return JsonResponse({"data": data})

def caretaker(request, pk):
    users = get_object_or_404(User, pk=pk)
    products = Lodges.objects.filter(available=True).order_by("-id")
    profile = get_object_or_404(Profile, pk=pk)


    context = {
        "users": users,
        "products":products,
        "profile":profile,  
    }

    if request.method == 'POST':
        
        form = ContactUs(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            message=request.POST['message'],
            user=request.user
        )
        form.save()
        html_template = 'core/email.html'
        html_message = render_to_string('core/email.html', {'form': form})
            #html_message = render_to_string(html_template)
        subject = 'welcome CareTaker'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [users.email]
        message = EmailMessage(subject, html_message,
                                   email_form, recipient_list)
        message.content_subtype = 'html'
        message.send()
        messages.success(request, "Message sent Successfully. We will get back to You")
        return redirect("core:caretaker", pk=users.id)
    else:
        
        return render(request, "core/caretaker.html", context)


