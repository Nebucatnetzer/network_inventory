from django.urls import path, include


urlpatterns = [
    # required for the login functionality
    path('accounts/', include('django.contrib.auth.urls')),
]
