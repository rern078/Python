from django.contrib import admin
from django.urls import path
from django.urls import re_path

from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', blog_views.home),
    re_path(r'^post/(?P<single>[-\w]+)/$', blog_views.single, name='single'),
#    path('username/<str:username>/', blog_views.home, name='username'),
]
