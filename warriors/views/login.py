from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from warriors.serializers import LoginUserSerializer, serializers
from warriors.models import User
from rest_framework.authtoken.models import Token

from django.views.generic import TemplateView, CreateView, View, ListView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


class SignUp(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            user = User.object.create_user(password=data['password'], email=data['email'],username=data['username'])
            token, create = Token.objects.get_or_create(user=user)
            return Response({token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self,request):
        try:
            data = request.data
            password = data['password']
            email = data['email']
            user = User.object.filter(email=email).first()
            if user is None:
                return Response("email is wrong ",status=status.HTTP_400_BAD_REQUEST)
            print(user)
            if user.check_password(raw_password=password):
                token = Token.objects.filter(user=user).first()
                data = {}
                data['token'] = token.key
                data['username'] = user.username
                data['id'] = user.id
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response("password is wrong",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            print(e)
            return Response("invalid data")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    try:
        data = request.data
        user = request.user
        password = data['password']
        new_password = data['new_password']
        if user.check_password(raw_password=password):
            user.set_password(raw_password=new_password)
            user.save()
            return Response( status=status.HTTP_200_OK)
        return Response("password is wrong", status=status.HTTP_400_BAD_REQUEST)
    except Exception as e :
        print(e)
        return Response("invalid data")


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class UsersList(ListView):
    model = User
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
