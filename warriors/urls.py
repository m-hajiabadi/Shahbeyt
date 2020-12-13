"""warriors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from warriors.views.login import *
from warriors.views.profile import *
from warriors.views.poem import *
from warriors.views.mainpage import *
# from warriors.warriors.views.login import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='sign_up'),
    path('login/', login, name='login'),
    path('user/profile/',user_profile, name=''),
    path('user/profile/update/',update_profile, name='update profile'),
    path('poem/<str:poem_id>/',show_poem, name='show poem'),
    path('addPoem/',add_poem, name='add poem'),
    # path('mainpage/top',top_users, name='top users'),
    path('mainpage/users',user_number, name='user number'),
    path('mainpage/poems',poem_number, name='poem number'),
]
