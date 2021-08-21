"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
app_name = 'music_app'
from .import views
urlpatterns = [
    path('',views.home1,name="home1"),
    path('signup/',views.home,name="home"),
    path('home/',views.category,name="category"),
    path("<int:id>", views.category_album, name='category_album'),
    path("album/<int:id>/", views.allsong, name='allsong'),
    path('addCategory/',views.addCategory,name="addCategory"),
    path('addalbum/',views.addAlbum,name="addalbum"),
    path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path("home/album/<int:album_id>/favourite/", views.favourite, name='favourite'),
    path('favourite/',views.favsong,name="favsong"),
    path('addsong/',views.addsong,name="addsong"),
    path('request/',views.songrequest,name="songrequest"),
    path('accept/<int:song_id>/',views.accept,name="accept"),
    path('reject/<int:song_id>/',views.reject,name="reject"),
]
#/home/ on template
#but if /home/ changed to /categoory/
#{% url 'music_app:category'  %}