from django.contrib import admin
from django.urls import path, include

from DRFTest import urls as DRFTestURLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('DRFTest/', include(DRFTestURLs)),
]
