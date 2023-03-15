from django.urls import path, include
from rest_framework import routers

from . import views
from snippets import views as snipped_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', snipped_views.snippet_list),
    path('snippets/<int:pk>/', snipped_views.snippet_detail),
    # url(r'', include('core.api.v1.urls', namespace='default')),
]
