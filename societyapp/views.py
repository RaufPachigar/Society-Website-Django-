from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Member, Notice, Event
from django.shortcuts import get_object_or_404



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
    
    
    
    return render(request,'index.html')


def members(request):
    return render(request, 'members.html')


def notice_list(request):
    notices = Notice.objects.order_by('-posted_date')  # List all notices ordered by date
    context = {
        'notices': notices,
    }
    return render(request, 'notice_list.html', context)


def notice_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        notice = Notice(title=title, content=content)
        notice.save()
        messages.success(request, "Notice created successfully!")
        return redirect('notice_list.html')  # Redirect to the notice list view
    return render(request, 'notice_form.html')

def notice_detail(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)  # Get a specific notice by ID
    return render(request, 'notice_detail.html', {'notice': notice})

def notice_delete(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, "Notice deleted successfully!")
        return redirect('notice_list.html')  # Redirect to the notice list view
    return render(request, 'notice_confirm_delete.html', {'notice': notice})

def notice_update(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    if request.method == 'POST':
        notice.title = request.POST.get('title')
        notice.content = request.POST.get('content')
        notice.save()
        return redirect('notice_detail', notice_id=notice.id) 
        messages.success(request, "Notice updated successfully!")# Redirect to the notice detail view
    return render(request, 'notice_form.html', {'notice': notice})



def events(request):
    return render(request, 'events.html')
