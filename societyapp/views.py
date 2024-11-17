from django.shortcuts import render,redirect,get_object_or_404
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
    recent_notices = Notice.objects.order_by('-posted_date')[:1]  # Last 5 notices
    upcoming_events = Event.objects.order_by('event_date')[:1]    # Next 5 upcoming events

    context = {
        'total_members': total_members,
        'total_notices': total_notices,
        'total_events': total_events,
        'recent_notices': recent_notices,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'dashboard.html', context)


def members(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login  ")
        return redirect('/auth/login')
    
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'members.html', context)


def notice_list(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login  ")
        return redirect('/auth/login')
    
    notices = Notice.objects.order_by('-posted_date')  # List all notices ordered by date
    context = {
        'notices': notices,
    }
            

    return render(request, 'notice_list.html', context)


def notice_create(request):
    if request.method == 'POST':
        Notice.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        messages.success(request, "Notice created successfully!")
        return redirect('notice_list')  # Redirect to the notice list view
    return render(request, 'notice_form.html')

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)  # Get a specific notice by ID
    return render(request, 'notice_detail.html', {'notice': notice})

def notice_delete(request, notice_id):
    if request.method == 'POST':
        Notice.objects.filter(id=notice_id).delete()
        messages.success(request, "Notice deleted successfully!")
        return redirect('notice_list')
    return redirect('notice_detail', notice_id=notice_id)

def notice_update(request, notice_id):
    """Update a notice by its ID."""
    notice = get_object_or_404(Notice, id=notice_id)

    if request.method == 'POST':
        notice.title = request.POST['title']
        notice.content = request.POST['content']
        notice.save()
        messages.success(request, "Notice updated successfully!")
        return redirect('notice_detail', notice_id=notice.id)

    return render(request, 'notice_form.html', {'notice': notice})



def event_list(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login  ")
        return redirect('/auth/login')
    events = Event.objects.order_by('event_date')  # List all events ordered by date
    context = {
        'events': events,
    }
    return render(request, 'event_list.html', context)


def event_create(request):
    if request.method == 'POST':
        Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            event_date=request.POST['event_date']
        )
        messages.success(request, "Event created successfully!")
        return redirect('event_list')  # Redirect to the event list view
    return render(request, 'event_form.html')


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Get a specific event by ID
    return render(request, 'event_detail.html', {'event': event})

def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.event_date = request.POST.get('event_date')  
        event.save()
        messages.success(request, "Event updated successfully!")
        return redirect('event_detail', event_id=event.id)  # Redirect to the event detail view
    return render(request, 'event_form.html', {'event': event})

def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect('event_list')  # Redirect to the event list view
    return redirect('event_detail', event_id=event.id)

