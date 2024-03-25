from django.urls import path

from . import views  # Assuming your views are in Users.views

urlpatterns = [
    path('register/', views.index, name='index'),

    # ... other user-related URL patterns
]