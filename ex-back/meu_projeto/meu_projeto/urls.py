from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/blog/', permanent=True)),
    path('blog/', include('blog.urls')),
]

handler403 = 'blog.views.permissao_negada_403' 
