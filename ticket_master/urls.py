from django.contrib import admin
from django.urls import path
from ticket_notes.views import homepage_view, bookmark_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='index'),
    path('bookmark_event/',bookmark_event, name='bookmark_event'),

]

