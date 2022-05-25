from django.urls import path
from . import views 



urlpatterns = [
    path ('',views.latest_5_days, name = '')
    ]    