from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
router =DefaultRouter()
router.register('paintingApi',views.PaintingViewSet)
urlpatterns = [
    path("", views.index),
    path("home",views.home, name="home"),
    path("add",views.addPaintings, name="addPaintings"),
    path("register",views.register,name="register" ),
    path("login",views.loginPage,name="login"),
    path("logout",views.logoutPage,name="logout"),
    path("artist",views.artist,name="artists"),
    path("painting/<int:key>/",views.painting,name="painting"),
    path("painting",views.painting,name="paintings"),
    path("",include(router.urls)),
    
]
