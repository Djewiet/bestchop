from django.urls import path, include, re_path
from rest_framework import routers
from .views import UserViewSet,ListCreateUserProfile,UpdateDeleteUserProfile, UserProfileViewSet


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    #permission_classes=(permissions.IsAuthenticated,),
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [

# api documentation
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),  # <-- Here
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  # <-- Here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),  # <-- Here

    #other paths
    path(r'', include(router.urls)),
    path(r'auth/', include('rest_auth.urls')),
    path('userprofile/', ListCreateUserProfile.as_view()),
    path('userprofile/<int:user_id>/<int:pk>/', UpdateDeleteUserProfile.as_view(), name='userprofile-detail'),

]