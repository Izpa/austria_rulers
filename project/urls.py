"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.views.generic import TemplateView

import project.settings as settings
from django.contrib import admin

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
]

v0_urlpatterns = [
    url(r'rulers/', include('project.apps.rulers.urls')),
]

api_urlpatterns = [
    url(r'v0/', include(v0_urlpatterns)),
]

urlpatterns.append(url(r'^api/', include(api_urlpatterns)))

urlpatterns += url(r'^$', TemplateView.as_view(template_name="index.html")),

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
