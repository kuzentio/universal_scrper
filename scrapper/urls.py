from django.conf.urls import url

from scrapper import views

urlpatterns = [
    url(r'^get_events/', views.get_events, name='get_events'),
]
