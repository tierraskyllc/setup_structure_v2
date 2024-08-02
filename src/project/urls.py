from django.contrib import admin
from django.urls import path
from pages.views import base, numbered_boxes, about_lama

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base),
    path('numbered_boxes/', numbered_boxes, name='numbered_boxes'),
    path('about_lama/', about_lama, name='about_lama'),
]
