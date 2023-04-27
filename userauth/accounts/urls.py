from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns...
    path('', views.select, name='login'),
    path('login/<int:id>', views.login_view, name='login'),
    path('signup/<int:id>', views.signup, name='signup'),
    path('dashboard/<int:id>', views.dashboard, name='signup'),
]
