from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('api.urls')),
    path("auth/", obtain_auth_token),
    path("logout/", LogoutView.as_view(), name="logout"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          Document_root=settings.MEDIA_ROOT)
