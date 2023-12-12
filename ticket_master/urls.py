from django.contrib import admin
from django.urls import path
from ticket_notes.views import homepage_view, notes_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='index'),
    path('notes/', notes_view, name='notes'),
]

