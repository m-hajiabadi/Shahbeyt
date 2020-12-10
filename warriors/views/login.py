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
            return Response({"token : ": token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def get_users(request):
#     users = User.objects.filter().by_order('score')
#     serializer = UserListSerializer(users,many = True)

@api_view(['POST'])
def login(request):
    try:
        data = request.data
        password = data['password']
        email = data['email']
        user = User.object.filter(email=email).first()

        print(user)
        if user.check_password(raw_password=password):
            token, create = Token.objects.get_or_create(user)
            return Response(token.key)
        else:
            return Response("login failed")
    except:
        return Response("invalid data")

#
# class HomeView(TemplateView):
#     template_name = 'index.html'
#
#
# class TryLogin(TemplateView):
#     template_name = 'try_login.html'
#
#
# class SignUpView(CreateView):
#     model = User
#     template_name = 'sign_up.html'
#     fields = ('username', 'email', 'password')
#
#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'user'
#         return super().get_context_data(**kwargs)
#
#     def form_valid(self, form):
#         user = form.save()
#         user.set_password(user.password)
#         user.save()
#         login(self.request, user)
#         return redirect('home')
#
#
# class SignInView(TemplateView):
#     template_name = 'sign_in.html'
#
#     def post(self, request):
#         email = request.POST['email']
#         password = request.POST['password']
#         # user = authenticate(email=email, password=password)
#         user = User.object.filter(email = email).first()
#         if user is not None:
#             if user.check_password(password):
#                 if user.is_active:
#                     login(request, user)
#
#                     return HttpResponseRedirect(reverse('home'))
#                 else:
#                     return HttpResponse("Your account is not active.")
#             else:
#                 print("Someone tried to login and failed")
#                 print("They used username: {} and passoword: {}".format(email, password))
#                 return HttpResponseRedirect(reverse('try_login'))
#         else :
#             print("user with this email not exist")
#             return HttpResponseRedirect(reverse('try_login'))

        # return render(request, 'sign_in.html', {})   


class SignOutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


class UsersList(ListView):
    model = User
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
