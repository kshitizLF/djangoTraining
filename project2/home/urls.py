from django.urls import path
# import home.views as views
from home import views

urlpatterns = [
    path("",views.Home.as_view(),name="home"),
    path("redirectToHome/<int:id>",views.Home2.as_view(),name="redirect"),
    path("book/<int:pk>",views.Home3.as_view(),name="detail"),
    path("books/",views.Home4.as_view(),name="bookList"),
    path("formBook/",views.Home5.as_view(),name="formBook"),
    path("formSuccess/",views.Home6.as_view(),name="successForm"),
    path("createBook/",views.Home7.as_view(),name="createBook"),
    path("deleteProtected/<int:pk>",views.Home9.as_view(),name="ProtectedDeleteBook"),
    path("deleteProtected/delete/<int:pk>",views.Home8.as_view(),name="DeleteBook")
]