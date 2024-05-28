from django.urls import path
from .views import *


urlpatterns = [
    path('create_event/', create_event, name='create_event'),
    path('show_events/', show_events, name='show_events'),
    path('show_all_events/', show_all_events, name='show_all_events'),
    path('event_detail/<int:event_id>/', event_detail, name='event_detail'),

]

