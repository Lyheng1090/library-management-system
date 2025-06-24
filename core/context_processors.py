"""
Context processors for the library management system.
These provide global template variables across all templates.
"""

from django.contrib.auth.models import User
from core.models import Book
from room_management.models import Room, RoomBooking
from django.db.models import Q
from datetime import date


def system_stats(request):
    """
    Provide system statistics for navigation sidebar.
    """
    try:
        # Calculate total books
        total_books = Book.objects.count()
        
        # Calculate active users (users who are active)
        active_users = User.objects.filter(is_active=True).count()
        
        # Calculate available rooms (rooms that are not under maintenance)
        available_rooms = Room.objects.filter(
            status__in=['available', 'occupied']
        ).count()
        
        # Calculate pending bookings (bookings that are pending approval)
        pending_bookings = RoomBooking.objects.filter(
            status='pending'
        ).count()
        
    except Exception as e:
        # If there's any error, provide default values
        total_books = 0
        active_users = 0
        available_rooms = 0
        pending_bookings = 0
    
    return {
        'total_books': total_books,
        'active_users': active_users,
        'available_rooms': available_rooms,
        'pending_bookings': pending_bookings,
    }
