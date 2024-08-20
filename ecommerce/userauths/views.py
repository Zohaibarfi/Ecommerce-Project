from django.shortcuts import render, redirect
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()
#User = settings.AUTH_USER_MODEL


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, Your account has been created.")
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            if new_user is not None:
                login(request, new_user)
            return redirect("core:index")  # Redirect to the homepage or another page
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, "userauths/sign-up.html", context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey you are already logged in.")
        print("User is authenticated, redirecting to homepage")
        return redirect("core:index")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user = User.objects.get(email=email)
            print(f"User found: {user}")
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")
            return redirect("userauths:sign-in")
            
            
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Your are logged in.")
            return redirect("core:index")
        else:
            messages.warning(request, "User does not exist. Sign Up.") 
            return redirect("userauths:sign-in")
        
    context = {
         
     }   
               
    return render(request, "userauths/sign-in.html", context)



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("userauths:sign-in")