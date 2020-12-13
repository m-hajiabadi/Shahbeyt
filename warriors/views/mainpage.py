from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from warriors.serializers import LoginUserSerializer, serializers, UserSerializer, UserSerializer_out
from warriors.settings import PROFILE_COMPLETE_SCORE

from warriors.models import  Poem
from ..models import User as UserModel

from rest_framework.authtoken.models import Token

from django.views.generic import TemplateView, CreateView, View, ListView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@api_view(['GET'])
def user_number(request):
    user_number = UserModel.object.all().count()
    return Response({"number": user_number})


@api_view(['GET'])
def poem_number(request):
    poem_number = Poem.objects.all().count()
    return Response({"number": poem_number})


# @api_view(['GET'])
# def top_users(request):
#     cnt = UserModel.object.all().count()
#     print(cnt)
#     users = UserModel.object.last()
#     # users = [dict(q) for q in users]
#     # def querySet_to_list(qs):
#     #     """
#     #     this will return python list<dict>
#     #     """
#     #     return [dict(q) for q in qs]
#     #
#     # def get_answer_by_something(request):
#     #     ss = Answer.objects.filter(something).values()
#     #     querySet_to_list(ss)  # python list return.(json-able)
#
#     # if User.object.all().count() > 6:
#     #     users = User.object.filter()
#     # else:
#     #     users = User.object.all().order_by('score')
#     # temp = []
#     # for i in users :
#     #     temp.append(i.object.get())
#     # print(temp)
#     # users = list (users)
#     print(users)
#     serializers = UserSerializer(data =users)
#     if serializers.is_valid():
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

