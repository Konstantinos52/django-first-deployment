from django.conf.urls import url , include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^posts/',include('post.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.PagedAccueil.as_view(), name= 'page_d_accueil'),
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.TestPageView.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPageView.as_view(), name='thanks'),
]
