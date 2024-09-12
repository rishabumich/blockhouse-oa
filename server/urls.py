from django.contrib import admin
from django.urls import include, path

print("Loading server/urls.py")

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('api/', include('api.urls')),  # API routes
]