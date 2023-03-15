from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views as api_views
from snippets import views as snippet_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', snippet_views.UserList.as_view()),
    path('users/<int:pk>/', snippet_views.UserDetail.as_view()),
    path('snippets/', snippet_views.SnippetList.as_view()),
    path('snippets/<int:pk>/', snippet_views.SnippetDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns) # Doesn't work with routers in urlpattersn. Use query in url as ?format=json meanwhile