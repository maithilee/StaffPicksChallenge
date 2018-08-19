from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('results.urls')),
    path('results/', include('results.urls')),
    path('admin/', admin.site.urls),
]
