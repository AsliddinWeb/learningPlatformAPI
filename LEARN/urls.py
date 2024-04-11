from django.contrib import admin
from django.urls import path, include

# Swagger UI
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Static settings
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Learning Platform API",
      default_version='v1',
      description="Learning Platform",
   ),
)

# Admin UI Custom
admin.site.site_title = "Learning Platform"
admin.site.site_header = "Learning Platform"
admin.site.index_title = "Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger UI
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API
    path('api/v1/auth/', include('auth_app.urls')),
    path('api/v1/course/', include('course_app.urls')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)