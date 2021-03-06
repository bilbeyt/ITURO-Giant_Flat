from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('video.urls')),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
