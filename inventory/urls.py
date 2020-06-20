from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('base.urls')),
    path('weapons/', include('weapon.urls')),
    path('system-site/', include('systemsite.urls')),
    

]
