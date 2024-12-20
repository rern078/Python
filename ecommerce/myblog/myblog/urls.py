from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.views import static as django_static
from django.views.static import serve
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', blog_views.home),
    re_path(r'^post/(?P<single>[-\w]+)/$', blog_views.single, name='single'),
    re_path(r'^category/(?P<category>[-\w]+)/$', blog_views.archive, name='category'),
    re_path(r'^images/(?P<path>.*)/$',serve, {'document_root': settings.BASE_DIR / 'images'}),
]
