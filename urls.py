from django.urls import path, include

urlpatterns = [
    path('authentication/', include('authentication.urls')),
]