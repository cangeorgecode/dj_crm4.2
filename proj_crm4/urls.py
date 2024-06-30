from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crm.urls')),
    path('users/', include('users.urls')),
    path('landing/', include('landingpage.urls')),
]
