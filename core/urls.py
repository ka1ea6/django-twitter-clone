from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('post', views.post, name='post'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name="login"),
    path('explore', views.explore, name='explore'),
    path('signup', views.signup, name='signup'),
    path('like', views.like_post, name='like_post')
]
