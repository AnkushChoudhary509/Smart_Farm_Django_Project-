from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from farming import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),

    # ── AUTH ──────────────────────────────────────────
    path('login/',  fv.login_view,  name='login'),
    path('signup/', fv.signup_view, name='signup'),
    path('logout/', fv.logout_view, name='logout'),

    # ── APP ───────────────────────────────────────────
    path('', include('farming.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
