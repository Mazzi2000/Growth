from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from journaling.views import JournalEntryViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'journal/entries', JournalEntryViewSet, basename='journal-entry')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]