
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework.routers import DefaultRouter
from gpsinfo.views import GPSLocationViewSet  # Adjust import based on your app name

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
    
router = DefaultRouter()
router.register(r'gpslocations', GPSLocationViewSet)

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoints
    # path('api/token/', include('rest_framework_simplejwt.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('accounts.urls')),
    path('', lambda request: redirect('login'), name='home'),  # Optional: redirect root to login
]
