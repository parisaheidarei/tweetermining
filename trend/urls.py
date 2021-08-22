from django.urls import path
from .views import getHashtags,getHashtagsDetail,viewIndex,viewHome, viewSecondTable, viewTable, viewTableFilter, viewTableSearch, viewTrend,viewChart, HomeView, get_data, ChartData,viewjsontable,viewjsonresponse
urlpatterns = [
    #path('',getHashtags),
    path('home',viewHome),
    path('<num>',getHashtagsDetail),
    path("index", viewIndex),
    path("trend", viewTrend),
    #path("chart", viewChart),
    #path("/charts/", views.HomeView.as_view(), name='home'),
    path("chart", viewChart.as_view(), name='home'),
    path("api/data/", get_data, name='api-data'),
    path("api/chart/data/", ChartData.as_view()),
    path("table", viewTable),
    path("table-search", viewTableSearch),
    path("secondtable", viewSecondTable),
    path("jsontable",viewjsontable.as_view(),name='jsontable'),
    path("jsonresponse",viewjsonresponse.as_view(),name='jsonresponse')


]