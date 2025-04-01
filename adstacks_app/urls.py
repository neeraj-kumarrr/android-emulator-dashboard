from django.urls import  path

from .views import AddAppView , GetAppView ,DeleteAppView

urlpatterns =[
    path("add-app/" , AddAppView.as_view() ,name ="add-app"),
    path("get-app/<int:id>/" , GetAppView.as_view(), name= "get-app"),
    path("delete-app/<int:id>/" ,DeleteAppView.as_view() ,name="delete-app"),

]

    

