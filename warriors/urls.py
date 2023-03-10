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
from django.conf import settings
from django.conf.urls.static import static
from warriors.views.poem import *
from warriors.views.login import *
from warriors.views.profile import *
from warriors.views.mainpage import *
from warriors.views.annotation import *

# from warriors.warriors.views.login import *
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/signup/', SignUp.as_view(), name='sign_up'),
                  path('api/login/', Login.as_view(), name='login'),
                  path('api/changepassword/', change_password, name='change password'),
                  path('api/user/profile/', user_profile, name='user profile'),
                  path('api/user/profile/update/', update_profile, name='update profile'),
                  path('api/user/profile/comments/<int:user_id>', user_comments, name='user comment'),
                  path('api/user/profile/poems/<int:user_id>', user_poems, name='user poems'),
                  path('api/user/profile/likedpoems/<int:user_id>', user_liked_poems, name='user liked poems'),
                  path('api/user/profile/getprofile/<int:user_id>', get_user_profile, name='get user profile'),
                  path('api/poem/<int:poem_id>/', show_poem, name='show poem'),
                  path('api/poem/all/', show_all_poem, name='show all poem'),
                  path('api/poem/delete/<int:poem_id>', delete_poem, name='delete poem'),
                  path('api/poem/likepoem/<int:poem_id>', like_poem, name='like poem'),
                  path('api/poem/removelike/<int:poem_id>', remove_like_poem, name='remove like poem'),
                  path('api/addPoem/', add_poem, name='add poem'),
                  path('api/search', search_beyts, name='search'),

                  path('api/annotation/add', add_annotation, name='add annotation'),
                  path('api/annotation/get/<int:poem_id>', get_poem_annotation, name='get  poem annotation'),
                  path('api/user/annotation/<int:user_id>', get_user_annotation, name='get user annotation'),

                  # path('mainpage/users',user_number, name='user number'),
                  path('api/mainpage/poems', poem_number, name='poem number'),
                  path('api/mainpage/randombeyt', random_beyt, name='random beyt'),
                  path('api/mainpage/newpoems', new_poems, name='new poems'),
                  path('api/mainpage/annotation', annotation_number, name='annotation number'),
                  path('api/mainpage/top', top_users, name='top users'),
                  path('api/mainpage/users', user_number, name='user number'),
                  # path('api/mainpage/newpoems',new_poems, name='new poems'),
                  path('api/poem/comments/<int:poem_id>', get_comment, name='get comments'),
                  path('api/poem/addcomment/', add_comment, name='add comment'),
                  path('api/poem/likednumber/<int:poem_id>', poem_liked_number, name='poem liked number'),
                  path('api/poem/likecomment/<int:comment_id>/<int:isLike>', like_or_dislike_comment,
                       name='like comment'),
                  path('api/poem/isuserliked/<int:poem_id>', is_user_liked_poem,name= 'is user liked poem'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
