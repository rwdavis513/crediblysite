import logging
from rest_framework import permissions, viewsets
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import IsAuthorOfPost
from posts.serializers import PostSerializer
from authentication.models import Account

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsAuthorOfPost(),)

    def perform_create(self, serializer):
        recipient = Account.objects.get(username=self.request.data['recipient'].lower())  # return the associated account with the entered username. Probably need to add validation here.
        # Need error validation. If the recipient can't be found return an error.
        # Need to add error message to AngularJS to note that the user can't be found.

        instance = serializer.save(author=self.request.user,recipient=recipient)

        return super(PostViewSet, self).perform_create(serializer)

    def get_serializer_context(self):
        return {'request': self.request}

class AccountPostsViewSet(viewsets.ViewSet):
    queryset = Post.objects.select_related('recipient').all()
    serializer_class = PostSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(recipient__username=account_username)
        serializer = self.serializer_class(queryset, many=True, context={'request':request})

        return Response(serializer.data)

