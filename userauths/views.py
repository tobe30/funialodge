from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from userauths.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.conf import settings


# Create your views here.

def reg(request):
    
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            html_template = 'core/register_email.html'
            html_message = render_to_string('core/register_email.html', {'form': form})
            #html_message = render_to_string(html_template)
            subject = 'welcome CareTaker'
            email_form = settings.EMAIL_HOST_USER
            recipient_list = [new_user.email]
            message = EmailMessage(subject, html_message,
                                   email_form, recipient_list)
            message.content_subtype = 'html'
            message.send()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, You account was created successfully.")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect("dashboard:index")
    else:
        form = RegisterForm()


    context = {
        'form': form,
    }
    return render(request, "userauths/register.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already Logged In.")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email") # peanuts@gmail.com
        password = request.POST.get("password") # getmepeanuts

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You are logged in.")
                return redirect("core:index")
            else:
                messages.warning(request, "User Does Not Exist, create an account.")
    
        except:
            messages.warning(request, f"User with {email} does not exist")
        

    
    return render(request, "userauths/login.html")
def logout_view(request):

    logout(request)
    messages.success(request, f"You logged out.")
    return redirect("core:index")
