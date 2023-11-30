from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register('categories', CategoryViewSet, basename='categories')
v1_router.register('genres', GenreViewSet, basename='genres')
v1_router.register('titles', TitleViewSet, basename='titles')
# v1_router.register('follow', FollowViewSet, basename='follows')
# v1_router.register('posts', PostViewSet, basename='posts')
# v1_router.register(r'posts/(?P<post_id>\d+)/comments',
#                    CommentViewSet,
#                    basename='comments')

urlpatterns = [
    # path('token/', get_token),
    # path('signup/', Signup.as_view(), name='signup'),
    path('auth/signup/', views.create_user),
    path('v1/', include(v1_router.urls)),
    # path('v1/jwt/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    # path('v1/', include('djoser.urls.jwt')),
]
