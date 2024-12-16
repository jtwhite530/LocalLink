from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm  
from django.contrib.auth.decorators import login_required  
from .models import Event
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Count


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def index_view(request):
    return render(request, 'index.html') 


def logout_view(request):
    logout(request)
    return redirect('login')  



@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        
        Event.objects.create(
            user=request.user,
            title=title,
            description=description,
            location=location,
            event_date=event_date,
            event_time=event_time
        )
        return redirect('home') 
    
    return render(request, 'home.html')
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count
from django.db.models import F


import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Count, F
from django.shortcuts import render
from .models import Event


#user home
def home_view(request):
    my_events = Event.objects.filter(user=request.user)
    my_events_list = list(my_events.values('title', 'location', 'event_date', 'event_time'))
    my_events_json = json.dumps(my_events_list, cls=DjangoJSONEncoder)

    all_events = Event.objects.all()  

    all_events_list = list(all_events.values('title', 'location', 'event_date', 'event_time'))
    all_events_json = json.dumps(all_events_list, cls=DjangoJSONEncoder)

    temp_events_list = list(all_events.values('title', 'location', 'event_date', 'event_time'))
    temp_events_json = json.dumps(temp_events_list, cls=DjangoJSONEncoder)

    city_event_count = (
        Event.objects
        .values(city=F('location'))  
        .annotate(event_count=Count('id'))
    )
    city_event_count_json = json.dumps(list(city_event_count), cls=DjangoJSONEncoder)

    return render(request, 'home.html', {
        'my_events': my_events,
        'all_events': all_events,  
        'my_events_json': my_events_json,
        'all_events_json': all_events_json,
        'temp_events_json': temp_events_json,
        'city_event_count_json': city_event_count_json,
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event  

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')  

from django.http import HttpResponse
from django.conf import settings
import os

def map_view(request):
    return render(request, 'map_content.html')