from django.contrib import admin
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url

admin.site.site_header = "E.Y | Blog Project Dashboard"
admin.site.site_title = "E.Y | Blog Project Dashboard"

urlpatterns = []
urlpatterns += i18n_patterns(url('admin/', admin.site.urls))
urlpatterns += i18n_patterns(url('accounts/', include("user.urls")))
urlpatterns += i18n_patterns(url('', include("core.urls")), prefix_default_language=True)
urlpatterns += i18n_patterns(url('', include("post.urls")), prefix_default_language=True)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

