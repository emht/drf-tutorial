from django.urls import path, include
from rest_framework import routers, renderers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views as api_views
from snippets.views import SnippetViewSet, UserViewSet

router = routers.DefaultRouter()
# router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'users', UserViewSet, basename='users')
router.register(r'snippets', SnippetViewSet, basename='snippet')

urlpatterns = [
    path('', include(router.urls))
]

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#         'get': 'highlight'
#     }, renderer_classes=[renderers.StaticHTMLRenderer]
# )
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


# urlpatterns = format_suffix_patterns([
#     # path('', include(router.urls)),
#     path('', snippet_views.api_root),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-hightlight'),
# ])

