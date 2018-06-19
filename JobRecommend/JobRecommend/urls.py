"""JobRecommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calc import views as calc_views
from zhilianjob import views as job_views

urlpatterns = [
    path('', job_views.index, name="index"),

    path('posin/', job_views.posin, name="posin"),
    path('workn/', job_views.workn, name="workn"),
    path('compn/', job_views.compn, name="compn"),
    path('sizen/', job_views.sizen, name="sizen"),
    path('attributen/', job_views.attributen, name="attributen"),
    path('fieldn/', job_views.fieldn, name="fieldn"),
    path('workedun/', job_views.workedun, name="workedun"),
    path('edusaln/', job_views.edusaln, name="edusaln"),
    path('expsaln/', job_views.expsaln, name="expsaln"),

    path('upload/', job_views.upload, name='upload'),
    path('result/', job_views.result, name='result'),

    path('test/', job_views.test, name="test"),
    path('new_add/<int:a>/<int:b>/', calc_views.add2, name='add2'),
    path('add/', calc_views.add, name='add'),

    path('admin/', admin.site.urls),
]
