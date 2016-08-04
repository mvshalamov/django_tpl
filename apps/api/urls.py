from django.conf.urls import url

from apps.api import views as api_views


urlpatterns = [
    url(
        regex=r'^ping/$',
        view=api_views.ping,
        name='ping'
    ),
    url(
        regex=r'^users/$',
        view=api_views.ListUsers.as_view(),
        name='list_users'
    ),
    url(
        regex=r'^users/(?P<pk>[0-9]+)/$',
        view=api_views.DetailUser.as_view(),
        name='detail_user'
    ),
]
