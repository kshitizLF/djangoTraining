from django.urls import path
from . import views

urlpatterns = [
    path('',views.funct,name="home"),
    path('polls',views.polls,name="polls"),
    path('quest/<int:id>',views.quest,name="questionDetail"),
    path('details/<int:id>',views.f1,name="details"),
    path('form',views.form,name="form"),
    path('formDone/',views.formSubmit,name="formSubmit")
]

# print(reverse('home'))