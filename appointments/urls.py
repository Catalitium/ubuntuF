from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_appointment, name='book_appointment'),  # Root URL points to the book_appointment view
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('success/', views.success, name='success'),  # Success page after booking
]
