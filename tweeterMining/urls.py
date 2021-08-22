"""tweeterMining URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from trend import views 
#from .views import IndexFormView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/', views.addUsers),
    #path('trend/',include('trend.urls'))
    path('getHashtags/', views.getHashtags),
    path('home/', views.viewHome),
    #path('index/',views.getHashtags)
    path('index/',views.viewIndex),
    path('trend/',views.viewTrend),
    #path('charts/',views.viewChart)
    path("chart/", views.viewChart.as_view(), name='home'),
    path("api/data/", views.get_data, name='api-data'),
    path("api/chart/data/", views.ChartData.as_view()),
    path('table/', views.viewTable),
    path('table-search/', views.viewTableSearch),
    path('secondtable/', views.viewSecondTable),
    path('table-filter/', views.viewTableFilter),
    path('jsontable/', views.viewjsontable.as_view(),name='jsontable'),
    path('jsonresponse/', views.viewjsonresponse.as_view(),name='jsonresponse')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
