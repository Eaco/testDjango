from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_view, name='login_view'),
    url(r'^login$', views.login_request, name='login_request'),
    url(r'^main$', views.main_view, name='main_view'),
]