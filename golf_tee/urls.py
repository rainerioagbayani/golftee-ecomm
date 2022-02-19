from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import IndexView


app_name = 'golf_tee'

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('', IndexView.as_view(), name='index'),
    
    # django-oscar-accounts https://github.com/django-oscar/django-oscar-accounts
    #path('dashboard/accounts/', apps.get_app_config('accounts_dashboard').urls),

    # Paypal
    path(r'^checkout/paypal/', include('paypal.express.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('admin/', admin.site.urls),
    path("", apps.get_app_config("oscar_promotions").urls),
    path("dashboard/promotions/", apps.get_app_config("oscar_promotions_dashboard").urls),

    path('', include(apps.get_app_config('oscar').urls[0])),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)