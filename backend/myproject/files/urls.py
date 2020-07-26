from django.conf.urls import url 
from files import views 
 
urlpatterns = [ 
    url(r'^api/files$', views.file_list),
    url(r'^api/files/(?P<pk>[0-9]+)$', views.file_detail),
    url(r'^api/files/published$', views.file_list_published)
]