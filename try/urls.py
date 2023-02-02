
from django.contrib import admin
from django.urls import path
from .views import a
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a, name='a'),
    
]
