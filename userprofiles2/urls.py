from django.conf.urls import url
from . import views
from .views import ProfileHomeView, ProfileIdentite
from django.urls import path

urlpatterns = [
    url(r'^$', ProfileHomeView.as_view(), name='profile-home'),
    url(r'^identity/(?P<pk>[0-9]+)/$',
        ProfileIdentite.as_view(), name='profile-identity-form'),
    path('addpill', views.get_pill, name='pills'),
    path('addpill/list', views.PillView.as_view(), name='pill-list'),
]
