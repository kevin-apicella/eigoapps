from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('syllableconnect/', include('syllableconnect.urls')),
    path('members/', include('members.urls')),
    path('', include('menu.urls'))
]
