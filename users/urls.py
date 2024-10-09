from django.urls import re_path, include
from rest_framework import routers

from users.views.user import UserViewSet

router = routers.DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    re_path('/', include(router.urls))
]
