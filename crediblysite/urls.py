from django.conf.urls import patterns, url, include
from crediblysite.views import IndexView
from rest_framework_nested import routers
from authentication.views import AccountViewSet, LoginView, LogoutView
from authentication.views import UserImageListView, UserImageDetailView
from posts.views import AccountPostsViewSet, PostViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/userImage/$', UserImageListView.as_view(), name='userimage-list'),
    url(r'^api/v1/auth/userImage/(?P<pk>[0-9]+)/$', UserImageDetailView.as_view(), name='userimage-detail'),

    #url(r'^api/v1/fileUpload/', FileUploadView.as_view(), name='fileUpload'),
    url(r'^api/v1/auth/login/$', LoginView.as_view(),name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('^.*$', IndexView.as_view(), name='index'),
)
