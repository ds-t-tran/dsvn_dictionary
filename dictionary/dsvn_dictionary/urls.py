from django.conf.urls import url 
from dsvn_dictionary import views 

urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorials/published$', views.tutorial_list_published),
    url(r'^api/vidictionary$', views.vidictionary_list)
]