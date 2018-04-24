from django.conf.urls import url, include
from webscraper import views
from .api import Rise_againstApi
 
app_name = "webscraper"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^show/$', views.show, name='show'),
    url(r'^rise$', Rise_againstApi.as_view())

    # url(r'^delete/(?P<document_id>[a-z0-9]*)/$', views.delete, name='delete'),
]