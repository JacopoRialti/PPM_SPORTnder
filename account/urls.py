from django.urls import path
from . import views

urlpatterns = [

    path("login_user", views.login_user, name="login"),
    path("signup_user", views.signup_user, name="signup"),
    path("logout_user", views.logout_user, name="logout"),
    path('register_event/<int:event_id>/', views.register_event, name='register_event'),
    path('unregister_event/<int:event_id>/', views.unregister_event, name='unregister_event'),

]
