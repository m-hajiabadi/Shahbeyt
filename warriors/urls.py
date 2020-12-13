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
    path('api/admin/', admin.site.urls),
    path('api/signup/', SignUp.as_view(), name='sign_up'),
    path('api/login/', Login.as_view(), name='login'),
    path('api/changepassword/', change_password, name='change password'),
    path('api/user/profile/',user_profile, name=''),
    path('api/user/profile/update/',update_profile, name='update profile'),
    path('api/poem/<str:poem_id>/',show_poem, name='show poem'),
    path('api/addPoem/',add_poem, name='add poem'),
    path('api/mainpage/top',top_users, name='top users'),
    path('api/mainpage/users',user_number, name='user number'),
    # path('mainpage/users',user_number, name='user number'),
    path('api/mainpage/poems',poem_number, name='poem number'),
    path('api/mainpage/randombeyt',random_beyt, name='random beyt'),
    path('api/mainpage/newpoems',new_poems, name='new poems'),
]
