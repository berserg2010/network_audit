from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', include('workstation_app.urls'), name='workstation'),

    path('admin/', admin.site.urls),
]
