from django.urls import path 
from . import views
urlpatterns = [
   path('', views.dashboard_view, name='dashboard'),
   path('Society-Members/', views.members, name='members'),
   path('Notice/', views.notice, name='Notice'),
   path('Events/', views.events, name='Events')

   
]
