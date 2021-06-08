from django.urls import include, path
from  .views import PerformanceListView
urlpatterns = [
    path('performances/',PerformanceListView.as_view(),name='performances-create-list')

]



