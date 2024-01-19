
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('desk/<int:id>',views.deskNo,name="deskNo"),
    path('tasks/<int:id>',views.getTasks,name="tasks")
]