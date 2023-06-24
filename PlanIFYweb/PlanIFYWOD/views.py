from django.shortcuts import render, HttpResponse, redirect
from .forms import EventForm, CreateUserForm, UserAccountForm, EventName
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserAccount, Event
from django.contrib.auth.models import User


@login_required(login_url='SignIn')
def home(request):
    usern = UserAccount.objects.filter(username=request.user).values()
    events = Event.objects.filter(event_host_user=int(usern[0]['user_id_number'])).values()
    form = EventName()
    if request.method == 'POST':
        form = EventName(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)

    return render(request, 'PlanIFYweb/dashboard.html', {'pagename':'Home', 'hostevents': events, 'form':form})


@login_required(login_url='SignIn')
def createnewevent(request):
    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('Home')


    return render(request, 'PlanIFYweb/newevent.html', {'pagename': 'New Event', 'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for: {username}')
                return redirect('CompleteRegistration', username)
            
            messages.error(request, 'There was an issue creating the account!')
            print(request)
        
        return render(request, 'PlanIFYweb/register.html', {'form': form})



def usersignin(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')

        return render(request, 'PlanIFYweb/signin.html')


def usersignout(request):
    logout(request)
    return render(request, 'PlanIFYweb/signin.html')



def completeregistration(request, username):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        user = User.objects.get(username=username)
        
        if request.method == 'POST':
            form = UserAccountForm(request.POST)
            if form.is_valid():
                form.cleaned_data['username'] = username
                print(form.cleaned_data['username'])
                form.save()
                uname = user.username
                password = user.password
                user = authenticate(request, username=uname, password=password)
                if user is not None:
                    login(request, user)
                return redirect('Home')
        
        else:
            user = User.objects.get(username=username)
            temp = user.username
            form = UserAccountForm(initial={'username': temp, 'first_name_user': user.first_name, 'last_name_user': user.last_name, 'email_user': user.email})
        return render(request, 'PlanIFYweb/finishregistration.html', {'form': form, 'username': username})