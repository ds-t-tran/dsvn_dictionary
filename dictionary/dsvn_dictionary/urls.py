from django.conf.urls import url 
from dsvn_dictionary import views 

urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/vidictionary$', views.vidictionary_list),
    url(r'^api/search/vidictionary$', views.vidictionary_search),
    url(r'^api/update/vidictionary/(?P<pk>[0-9]+)$', views.vidictionary_update),
    url(r'^api/delete/vidictionary/(?P<pk>[0-9]+)$', views.vidictionary_delete),
    url(r'^api/jadictionary$', views.jadictionary_list),
    url(r'^api/search/jadictionary$', views.jadictionary_search),
    url(r'^api/update/jadictionary/(?P<pk>[0-9]+)$', views.jadictionary_update),
    url(r'^api/delete/jadictionary/(?P<pk>[0-9]+)$', views.jadictionary_delete),
]