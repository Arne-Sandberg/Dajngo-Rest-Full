from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from Serializers.api.viewsets import SerializersViewSet

# API Router v1
router = routers.SimpleRouter()
router.register(r'serializers', SerializersViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include(router.urls)),
] 
