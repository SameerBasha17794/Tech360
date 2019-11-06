"""Tech360 URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import (index,coursecontent,uploadcoursecontent,uploadsubcourse,base,blogs,uploadblogs,blog_detail,website,
signup_login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', index,name='index'),
    path('courses/<name>/',coursecontent,name='coursecontent'),
    path('uploadcoursecontent/',uploadcoursecontent,name='uploadcoursecontent'),
    path('uploadsubcourse/',uploadsubcourse,name='uploadsubcourse'),
    path('base/',base,name='base'),
    path('blogs/',blogs,name='blogs'),
    path('uploadblogs/',uploadblogs,name='uploadblogs'),
    path('blogs/<name>/',blog_detail,name='blog_detail'),
    path('website/',website,name='website'),
    path('signup_login/',signup_login,name='signup_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)