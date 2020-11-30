from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users-in-ad-group',
                views.UserInAdGroupViewSet,
                'user-in-ad-group')
router.register(r'users-in-mail-group',
                views.UserInMailGroupViewSet,
                'user-in-mail-group')
router.register(r'ad-groups',
                views.AdGroupViewSet,
                'ad-group')
router.register(r'mail-groups',
                views.MailGroupViewSet,
                'mail-group')
router.register(r'mail-alias',
                views.MailAliasViewSet,
                'mail-alias')


urlpatterns = [
    # required for the login functionality
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
