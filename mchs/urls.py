from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'main.views.view_404'



# staff_patterns = ([
#     path('staff-admin/', admin.site.urls, name='staff'),
# ], 'staffa')

urlpatterns = [
    path('staff-admin/', admin.site.urls),
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
