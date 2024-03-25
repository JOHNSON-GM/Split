from django.urls import path


from . import views  # Assuming your views are in Users.views

urlpatterns = [
    path('add_expense/', views.Add, name='add'),

    # ... other user-related URL patterns
]