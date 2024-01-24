from django.urls import path
from . import api_views
from .views import postCarData
urlpatterns = [
    path("",api_views.hello,name="Hello"),
    # path("Cars/",api_views.GetData.as_view(),name="Cars")
    path("Cars/",api_views.getData,name="Cars"),
    path("postCar/",postCarData.as_view(),name="insertCar"),
    path("postCarjson/",api_views.postData,name="jsonPost"),
    path("deleteCar/<str:model>",api_views.carDelete,name="delete"),
    path("updateCar/<int:id>",api_views.carUpdate,name="update")
]