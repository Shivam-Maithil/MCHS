from django.urls import path
from .views import index, event, gallery

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('activities&Events/', event, name="event"),
    path('activities&Events/gallery/<id>/', gallery, name="gallery")
]
