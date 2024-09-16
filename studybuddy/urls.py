
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(reqyest):
    return HttpResponse('Home page')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
]
