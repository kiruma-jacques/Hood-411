from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='home'),
    url(r'your_hood/(\d+)/', views.hood_details, name='hood_details'),
    url(r'^profile/$', views.myProfile, name='profile'),
    url(r'^search/$', views.search_biz, name='search_biz'),
]
