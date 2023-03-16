from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(many=True, view_name='api:v1:user-detail', read_only=True) # Had to explicitly declare due to different namespacing
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='api:v1:snippet-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

        
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(many=True, view_name='api:v1:snippet-detail', read_only=True) # Had to explicitly declare due to different namespacing
    hightlight = serializers.HyperlinkedIdentityField(view_name='api:v1:snippet-highlight', format='html')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ['url', 'id', 'title', 'code', 
                  'linenos', 'language', 'style', 
                  'owner', 'hightlight']
