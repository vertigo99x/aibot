
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('backend/accounts/', include('accounts.urls')),
    path('backend/api/v1/', include('api.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

