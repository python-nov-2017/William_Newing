from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_login.urls')),
]
