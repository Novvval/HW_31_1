from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from HW_31_1 import settings
from ads.views.location import LocationViewSet
from ads.views.selection import SelectionListView, SelectionDetailView, SelectionUpdateView, SelectionDeleteView, \
    SelectionCreateView
from ads.views.service import index
from ads.views.ad import AdListView, AdCreateView, AdDetailView, AdUpdateView, AdDeleteView, AdUploadImageView
from ads.views.category import CategoryViewSet
from ads.views.user import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView


router = routers.SimpleRouter()
router.register("location", LocationViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path('', index, name="index"),

    path("ad/", AdListView.as_view(), name="ads"),
    path("ad/create/", AdCreateView.as_view(), name="ads_create"),
    path("ad/<int:pk>/", AdDetailView.as_view(), name="ad"),
    path("ad/<int:pk>/update/", AdUpdateView.as_view(), name="update_ad"),
    path("ad/<int:pk>/delete/", AdDeleteView.as_view(), name="delete_ad"),
    path("ad/<int:pk>/upload_image/", AdUploadImageView.as_view(), name="upload_image"),

    path("user/", UserListView.as_view(), name="users"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user"),
    path("user/create/", UserCreateView.as_view(), name="create_user"),
    path("user/<int:pk>/update/", UserUpdateView.as_view(), name="update_user"),
    path("user/<int:pk>/delete/", UserDeleteView.as_view(), name="delete_user"),
    path('user/token/', TokenObtainPairView.as_view(), name="get token"),
    path('user/token/refresh/', TokenRefreshView.as_view(), name="refresh token"),

    path("selection/", SelectionListView.as_view(), name="view selections"),
    path("selection/create/", SelectionCreateView.as_view(), name="create selection"),
    path("selection/<int:pk>/", SelectionDetailView.as_view(), name="view selection"),
    path("selection/<int:pk>/update/", SelectionUpdateView.as_view(), name="update selection"),
    path("selection/<int:pk>/delete/", SelectionDeleteView.as_view(), name="delete selection"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += router.urls
