from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name='home'),
    path("send_html_email/", views.send_html_email, name="send_html_email"),
]
