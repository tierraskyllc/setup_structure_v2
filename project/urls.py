from django.contrib import admin
from django.urls import path
from pages.views import base, numbered_boxes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('numbered_boxes/', numbered_boxes),
]
