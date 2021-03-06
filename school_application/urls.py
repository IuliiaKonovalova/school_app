"""school_application URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('profiles/', include('profiles.urls')),
    path('students/', include('students.urls')),
    path('sales/', include('sales.urls')),
    path('lessons/', include('lessons.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'school_application.views.handler404'
handler500 = 'school_application.views.handler500'
