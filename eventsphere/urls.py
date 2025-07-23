from django.contrib import admin
from django.urls import path, include
from events.api_views import EventViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/events', EventViewSet)
router.register('api/bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ⬇️ Include views from events app
    path('', include('events.urls')),

    # ⬇️ Include views from accounts app
    path('accounts/', include('accounts.urls')),

    # ⬇️ API endpoints
    path('', include(router.urls)),
]
