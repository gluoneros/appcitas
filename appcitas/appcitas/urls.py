"""Platzigram URLs module."""

# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from appcitas import views as local_views
from citas import views as citas_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    path('citas/', citas_views.list_citas),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)