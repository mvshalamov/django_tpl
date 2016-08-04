from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('apps.api.urls', namespace='api')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
