# events/urls.py
from django.urls import path
from .views import dashboard, book_event, cancel_booking, create_event, edit_event, delete_event
from .views import booking_history

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('book/<int:event_id>/', book_event, name='book'),         # ✅ Must exist
    path('cancel/<int:event_id>/', cancel_booking, name='cancel'),
    path('create/', create_event, name='create_event'),
    path('edit/<int:event_id>/', edit_event, name='edit_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
    path('history/', booking_history, name='booking_history'),
]
