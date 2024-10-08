
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mblog.urls')),
    path('signup/', include('django.contrib.auth.urls')),
    path('signup/', include('signup.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
