from django.urls import path 
from . import views
urlpatterns = [
   path('', views.dashboard_view, name='dashboard'),
   path('Society-Members/', views.members, name='members'),
   path('Notice/', views.notice_list, name='notice_list'),
   path('Notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
   path('Notice/create/', views.notice_create, name='notice_create'),
   path('Notice/<int:notice_id>/delete/', views.notice_delete, name='notice_delete'),
   path('Notice/<int:notice_id>/edit/', views.notice_update, name='notice_update'),
   path('Events/', views.event_list, name='event_list'), 
   path('Events/create/', views.event_create, name='event_create'),  
   path('Events/<int:event_id>/', views.event_detail, name='event_detail'), 
   path('Events/<int:event_id>/edit/', views.event_update, name='event_update'),  
   path('Events/<int:event_id>/delete/', views.event_delete, name='event_delete'),  

   
]
