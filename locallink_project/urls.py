from django.urls import path
from .views import index_view, login_view, register, home_view, logout_view
from . import views  
from .views import delete_event
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


def serve_image(request):
    image_path = '/home/jamesonw/LocalLink/media/logo.png'  
    return FileResponse(open(image_path, 'rb'), content_type='image/png')


urlpatterns = [
    path('', index_view, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'), 
    path('create-event/', views.create_event, name='create_event'),  
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('load-map/', views.map_view, name='load_map'),



 ] 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
