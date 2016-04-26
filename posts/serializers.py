from rest_framework import serializers
from authentication.serializers import AccountSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = AccountSerializer(read_only=True, required=False)
    recipient = AccountSerializer(read_only=True, required=False)

    created_at = serializers.SerializerMethodField()

    def get_created_at(self, instance):
        return instance.created_at.strftime("%m/%y")


    class Meta:
        model = Post

        fields = ('id', 'author', 'recipient', 'relationship', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_validation_exclusions(self, *args, **kwargs):
        exclusions = super(PostSerializer, self).get_validation_exclusions()

        return exclusions + ['author']