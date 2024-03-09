from django.contrib import admin
from django.urls import path

from project.views import home_page

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)