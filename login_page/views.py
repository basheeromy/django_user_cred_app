from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .froms import UserRegisterForm
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request):
    if 'userid' in request.session:
        return redirect('home_view') 
    if request.method == 'POST':
        usernm = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(username = usernm,password = passwd)
        userid = user.id
        print(f'user id is {userid}')
        
        if user is not None:
            request.session['userid'] = userid
            return redirect('home_view')
        else:
            print("invalid credentials !")
    return render(request,'login_page/login.html')

def sign_up_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            messages.success(request, f"Account created succefully for {fname} {lname}.")
            return redirect('login_page')
    else:
        form = UserRegisterForm()
        
    return render(request,'login_page/sign_up.html',{'form':form})

def log_out_view(request):
    if 'userid' in  request.session:
        request.session.flush()
    return redirect('login_page')
    