from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import login

from . import views

app_name='data'

urlpatterns = [
    # /data/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /data/123  <--book.id
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /data/book/add/
    url(r'book/add/$', views.BookCreate.as_view(), name='book-add'),

    # /data/book/123/
    url(r'book/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(), name='book-update'),

    # /data/book/123/delete/
    url(r'book/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),

    # /data/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /data/login
    url(r'^login/$', views.login_view, name='login'),
    
]
