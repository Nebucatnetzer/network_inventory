from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users-in-ad-group', views.UserInAdGroupViewSet)
router.register(r'users-in-mail-group', views.UserInMailGroupViewSet)
router.register(r'ad-groups', views.AdGroupViewSet)
router.register(r'mail-groups', views.MailGroupViewSet)
router.register(r'mail-alias', views.MailAliasViewSet)
