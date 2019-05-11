from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^new$', views.new),
    # url(r'^create$', views.index),
    # url(r'^(?P<number>[0-9]+)$', views.show),
    # url(r'^(?P<number>[0-9]+)/(?P<edit>\w+)$', views.edit),
    # url(r'^(?P<number>[0-9]+)/(?P<delete>\w+)$', views.destroy),
]