from django.urls import path
from .views import *


urlpatterns = [
    path('create_event/', create_event, name='create_event'),
    path('show_events/', show_events, name='show_events'),
    path('show_all_events/', show_all_events, name='show_all_events'),
    path('event_detail/<int:event_id>/', event_detail, name='event_detail'),
    path('edit_event/<int:event_id>/', edit_event, name='edit_event'),
    path('remove_user_from_event/<int:event_id>/<int:user_id>/', remove_user_from_event, name='remove_user_from_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),
]

