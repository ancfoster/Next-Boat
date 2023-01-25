from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from listings.views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("listings.urls"), name="listings-urls"),
    path('', include("conversations.urls"), name="conversation-urls"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'listings.views.handler404'
handler500 = 'listings.views.handler500'
