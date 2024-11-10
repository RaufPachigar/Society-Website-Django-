from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Member, Notice, Event



# Create your views here.
def dashboard_view(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login  ")
        return redirect('/auth/login')
    
    total_members = Member.objects.count()
    total_notices = Notice.objects.count()
    total_events = Event.objects.count()
    recent_notices = Notice.objects.order_by('-posted_date')[:5]  # Last 5 notices
    upcoming_events = Event.objects.order_by('event_date')[:5]    # Next 5 upcoming events

    context = {
        'total_members': total_members,
        'total_notices': total_notices,
        'total_events': total_events,
        'recent_notices': recent_notices,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'dashboard.html', context)
    
    
    
    return render(request,'index.html')