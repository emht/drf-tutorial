from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views as api_views
from snippets import views as snippet_views

# router = routers.DefaultRouter()
# router.register(r'users', api_views.UserViewSet)
# router.register(r'groups', api_views.GroupViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', snippet_views.api_root),
    path('users/', snippet_views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', snippet_views.UserDetail.as_view(), name='user-detail'),
    path('snippets/', snippet_views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', snippet_views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_views.SnippetHighlight.as_view(), name='snippet-hightlight'),
]

# urlpatterns = format_suffix_patterns(urlpatterns) # Doesn't work with routers in urlpattersn. Use query in url as ?format=json meanwhile