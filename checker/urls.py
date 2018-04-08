"""OnlineChecker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from checker.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', home),
    url(r'^create/$', createtest),
    url(r'^viewtest/$', viewtest),
    url(r'^create/(?P<class_section>[0-9A-Z]+)$', createtestclass),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)$', classtests),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)$', viewpaper),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/(?P<ques_id>[0-9]+)/addparameter$', addparameter),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/upload$', uploadpaper),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/upload/(?P<stu_id>[0-9]+)/submit$', submitpaper),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/upload/(?P<stu_id>[0-9]+)/viewupload', viewupload),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/upload/(?P<stu_id>[0-9]+)/check', checkupload),
    url(r'^viewtest/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/upload/(?P<stu_id>[0-9]+)/submitmarks', submitmarks),
    url(r'^create/(?P<class_section>[0-9A-Z]+)/add/$', registerpaper),
    url(r'^viewmarks/$', classesviewmarks),
    url(r'^viewmarks/(?P<class_section>[0-9A-Z]+)$', testsviewmarks),
    url(r'^viewmarks/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/$', studentsviewmarks),
    url(r'^viewmarks/(?P<class_section>[0-9A-Z]+)/(?P<paper_id>[0-9]+)/(?P<stu_id>[0-9]+)/$', viewmarks),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
