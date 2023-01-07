from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
