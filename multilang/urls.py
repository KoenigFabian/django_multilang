from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    #path('testapp/', include('testapp.urls')),
    path('admin/', admin.site.urls),
    #url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'', include('testapp.urls', namespace='testapp')),
    )
