from django.conf.urls import *
from django.urls import path, include


urlpatterns = [
    path('', include(('api.v1.urls', 'api'), namespace='default')),
    path('v1/', include(('api.v1.urls', 'api'), namespace='v1')),
    path('auth/', include('rest_framework.urls', namespace='api_auth'))
]