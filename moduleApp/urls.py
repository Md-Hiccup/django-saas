from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'create-module', views.create_module, name='create-module'),
    url(r'create-submodule', views.edit_module, name='edit-module'),
    url(r'random', views.random_page, name='random_page'),
    url(r'common/(?P<pk>[0-9]+)/$', views.common_page, name='common_page'),
]