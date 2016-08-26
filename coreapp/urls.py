from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^students/$', views.StudentList.as_view(), name='home'),
]
