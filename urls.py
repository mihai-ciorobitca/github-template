from django.urls import path, include

urlpatterns = [
    path('authentication/', include('authentication.urls')),
    path('', views.home, name='home'),
]