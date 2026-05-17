"""
SAVtech Solutions — Main URL Configuration
Routes all app URLs through their respective prefixes.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def home_redirect(request):
    """Redirect root URL to login or dashboard."""
    if request.user.is_authenticated:
        return redirect('accounts:role_redirect')
    return redirect('accounts:login')


urlpatterns = [
    # ─── Home ──────────────────────────────────────────────────────────
    path('', home_redirect, name='home'),

    # ─── Django Admin ──────────────────────────────────────────────────
    path('django-admin/', admin.site.urls),

    # ─── SAVtech Apps ──────────────────────────────────────────────────
    path('accounts/', include('accounts.urls')),
    path('repairs/', include('repairs.urls')),
    path('multisite/', include('multisite.urls')),

    # ─── Person 2 Apps (skeleton — to be implemented by Saad) ─────────
    # path('tracking/', include('tracking.urls')),
    # path('parts/', include('parts.urls')),
    # path('invoicing/', include('invoicing.urls')),
    # path('notifications/', include('notifications.urls')),

    # ─── Person 3 Apps (placeholder — to be implemented by Ahmed) ─────
    path('dashboard/', include('dashboard.urls')),
    path('ai/', include('ai_engine.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customize Django Admin
admin.site.site_header = "SAVtech Solutions — Administration"
admin.site.site_title = "SAVtech Admin"
admin.site.index_title = "Panneau d'administration"
