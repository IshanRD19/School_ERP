"""SchoolERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^home/(?P<index>[0-9]+)$', views.home),
    url(r'^multiplechoice/(?P<index>[0-9]+)/', include('Question_Bank.urls')),
    url(r'^assignment/(?P<index>[0-9]+)/(?P<sub>[0-9]+)$', views.assignment),
    url(r'^assignment/(?P<index>[0-9]+)/(?P<sub>[0-9]+)/add$', views.add_assignment),
    url(r'^assignment/(?P<index>[0-9]+)/(?P<sub>[0-9]+)/pushdata$', views.push_data_assignment),
    url(r'^assignment/(?P<index>[0-9]+)/(?P<id>[0-9]+)/grade$', views.grade_assignment),
    url(r'^assignment/(?P<index>[0-9]+)/(?P<id>[0-9]+)/updategrade$', views.update_grade),
    url(r'^class/(?P<index>[0-9]+)/(?P<classid>[A-Z0-9]+)$', views.view_class),
    url(r'^viewstudent/(?P<studentreg>[A-Z0-9]+)$', views.view_student),
]
