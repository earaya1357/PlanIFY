from django.shortcuts import render, HttpResponse, redirect
from .forms import EventForm, CreateUserForm, UserAccountForm, EventName, AffiliateSearch, FullEventForm, EventWorkoutForm, UserProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserAccount, Event, EventWorkOut, EventHelp, EventParticipant
from django.contrib.auth.models import User


#Registion page for new users to sign up for the site.
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


#Full registration page for new users
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
    

#Sign in page for all users
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

#Sign out page for all users
def usersignout(request):
    logout(request)
    return render(request, 'PlanIFYweb/signin.html')


def checkstatus(request):
    usern = UserAccount.objects.filter(username=request.user).values()
    athlete_approved = usern[0]['athlete_user_approved']
    host_approved = usern[0]['host_user_approved']
    vendor_approved = usern[0]['vendor_user_approved']
    return athlete_approved, host_approved, vendor_approved


#User profile page
@login_required(login_url='SignIn')
def userprofile(request, user):
    usern = UserAccount.objects.filter(username=request.user).values()
    profile = UserProfileForm(instance=user)

    return render(request, 'PlanIFYweb/profile.html', {'profile': profile})

#Home page for users
@login_required(login_url='SignIn')
def home(request):
    usern = UserAccount.objects.filter(username=request.user).values()
    athlete, host, vendor = checkstatus(request)

    
    #Filter events if the user is an athlete and has signed up for events
    if athlete:
        athleteevents = Event.objects.filter(event_host_user=int(usern[0]['user_id_number'])).values()
    else:
        athleteevents = None

    #Filter events if the user is a host and has created events
    if host:
        hostevents = Event.objects.filter(event_host_user=int(usern[0]['user_id_number'])).values()
    else:
        hostevents = None

    #Filter events if the user is a vendor and has signed up to cater events
    if vendor:
        vendorevents = Event.objects.filter(event_host_user=int(usern[0]['user_id_number'])).values()
    else:
        vendorevents = None
    
    form1 = EventName()
    form2 = AffiliateSearch()
    #Listen for POST requests and determine which form is being submitted
    if request.method == 'POST':
        if 'name' in request.POST:
            form1 = EventName(request.POST)
            if form1.is_valid():
                data = form1.cleaned_data['name']
                
                return redirect('EventDesign', data)
        
        elif 'affiliate_name' in request.POST:
            form2 = AffiliateSearch(request.POST)
            if form2.is_valid():
                data = form2.cleaned_data['affiliate_name']
                print(data)
            

    return render(request, 'PlanIFYweb/dashboard.html', {'pagename':'Home', 'hostevents': hostevents, 'athleteevents': athleteevents, 'vendorevents': vendorevents,'form1':form1, 'form2':form2})


@login_required(login_url='SignIn')
def eventdesign(request, eventname):
    usern = UserAccount.objects.filter(username=request.user).values()[0]['user_id_number']
    form = EventForm(initial={'event_host_user': usern,'event_name': eventname})

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            
            form.save()
            
            return redirect('Home')


    return render(request, 'PlanIFYweb/eventdesign.html', {'pagename': eventname, 'form': form})



@login_required(login_url='SignIn')
def hostedevents(request, id):
    usern = UserAccount.objects.filter(username=request.user).values()[0]['user_id_number']
    event = Event.objects.get(event_id=id)
    form = FullEventForm(instance=event)
    form2 = EventWorkoutForm(instance=event)
    workouts = EventWorkOut.objects.filter(event=id)

    if request.method == 'POST':
        try:
            if request.POST.get('workout_name'):
                form2 = EventWorkoutForm(request.POST, request.FILES)
                if form2.is_valid():
                    form2.save()
                    
    
            elif request.POST.get('event_name'):
                form = FullEventForm(request.POST, request.FILES, instance=event)
                if form.is_valid():
                    form.save()
                    
        except Exception as e:
            print(e)



    return render(request, 'PlanIFYweb/hostevent.html', {'pagename': event, 'form': form, 'form2': form2, 'workout_list': workouts})


#Page to allow host users to get prepared for an event 
@login_required(login_url='SignIn')
def prepareevent(request, event):
    usern = UserAccount.objects.filter(username=request.user).values()[0]['user_id_number']
    event = Event.objects.get(event_name=event)
    workoutlist = EventWorkOut.objects.filter(event=event)
    help = EventHelp.objects.filter(event=event)
    athletes = EventParticipant.objects.filter(event_id_number=event)
    print(help)

    return render(request, 'PlanIFYweb/eventprepare.html', {'pagename': event, 'workoutlist':workoutlist, 'help': help, 'athletes':athletes})

#General serach page for events. 
def generalevent(request, event):
    pass


#Landing page for all visitors.
def homepage(request):
    return render(request, 'PlanIFYweb/home.html')
