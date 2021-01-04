from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from warriors.serializers import LoginUserSerializer, serializers, UserSerializer, UserSerializer_out, \
    PoemSerializer_out, BeytSerializer_out

from warriors.settings import PROFILE_COMPLETE_SCORE, TOP_USER_NUMBERS
import random
from ..models import User as UserModel, Poem, Beyt, Annotation
from ..serializers import PoemSerializer
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

@api_view(['GET'])
def annotation_number(request):
    annotation_number = Annotation.objects.all().count()
    return Response({"number": annotation_number})

@api_view(['GET'])
def new_poem(request):
    poem = Poem.objects.last()
    serializers = PoemSerializer_out(poem)
    return Response(serializers.data, status=status.HTTP_200_OK)
    # return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def top_users(request):
    if UserModel.object.all().count() > TOP_USER_NUMBERS:
        users = UserModel.object.all().order_by('-score')[:6]
    else:
        users = UserModel.object.all().order_by('-score')
    print(users)
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


def pick_random_object():
    return random.randrange(1, Beyt.objects.all().count() + 1)


@api_view(['GET'])
def random_beyt(request):
    beyt = None
    while beyt != None:
        beyt = Beyt.objects.filter()[pick_random_object()]
    serializers = BeytSerializer_out(beyt)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def new_poems(request):
    beyt = Beyt.objects.filter(isKing=True)
    cnt = beyt.count()
    if beyt.count() > 3:
        beyt = beyt[cnt -3:cnt]
    serializers = BeytSerializer_out(beyt, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)
