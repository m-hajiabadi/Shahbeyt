from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from  warriors.serializers import LoginUserSerializer, serializers, UserSerializer, UserSerializer_out
from warriors.settings import PROFILE_COMPLETE_SCORE

from warriors.models import User
from rest_framework.authtoken.models import Token

from django.views.generic import TemplateView, CreateView, View, ListView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



def users_number():
    user_number = User.object.all().count()
    return Response({"number":user_number})