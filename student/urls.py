from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'^$', views.studentlogin, name='studentlogin'),
    url(r'home/(?P<index>[0-9]+)$', views.home),
    url(r'(?P<index>[0-9]+)/subject/(?P<subcode>[0-9A-Z]+)', views.view_subject_info)
]