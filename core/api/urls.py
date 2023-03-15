from django.conf.urls import *
from django.urls import path, include


urlpatterns = [
    path('', include(('api.v1.urls', 'default'), namespace='default')),
    path('v1/', include(('api.v1.urls', 'v1'), namespace='v1')),
]