"""evaluation URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^$', index, name='multiplechoicehome'),
    url(r'^createtest/$', createtest),
    url(r'^createtest/uploadquestions/$', uploadquestions, name="uploadquestionshome"),
    url(r'^createtest/createquestionpaper/$', createquestionpaper),
    url(r'^createtest/editquestions/$', editquestions),
    url(r'^createtest/editquestionpaper/$', editquestionpaper),
    url(r'^createtest/editquestionpaper/(?P<questionpaper_id>[0-9]+)/$', questionpaperid),
    url(r'^createtest/editquestionpaper/(?P<questionpaper_id>[0-9]+)/edit/$', questionpaperedit),
    url(r'^createtest/editquestions/(?P<question_id>[0-9]+)/$', editquestionid),
    url(r'^createtest/editquestions/(?P<question_id>[0-9]+)/edit/$', questionedit),
    url(r'^createtest/createquestionpaper/create/$', submitquestionpaper),
    url(r'^createtest/uploadquestions/submit/$', submitquestions),
    # accessed by student
    url(r'^taketest/$', taketest),
    url(r'^taketest/(?P<questionpaper_id>[0-9]+)/$', attempttest),
    url(r'^taketest/(?P<questionpaper_id>[0-9]+)/createlog/$', createlog),
    url(r'^(?P<questionpaper_id>[0-9]+)/(?P<session_id>[0-9]+)/testresult/$', testresult),
    url(r'^logs/', logs),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)