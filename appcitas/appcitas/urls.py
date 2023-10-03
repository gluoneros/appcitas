"""app citas modules"""
from django.urls import path
from appcitas import views as local_views
from citas import views as citas_views




urlpatterns = [
    
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sort_integers ),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    
    path('citas/', citas_views.list_citas),
    
]
