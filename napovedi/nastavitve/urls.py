from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # Examples:

    # url(r'^blog/', include('blog.urls')),


    url(r'^forecasting/', include('forecasting.urls')),
    url(r'^api2/', include('API2.urls')),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
