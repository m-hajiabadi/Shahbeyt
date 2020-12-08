from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from warriors.serializers import LoginUserSerializer, serializers, UserSerializer
from warriors.models import User
from rest_framework.authtoken.models import Token

from django.views.generic import TemplateView, CreateView, View, ListView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# class profile(APIView):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     def post(self,request):
#         pass
#     def get(self,request):
#         pass

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    if user is None:
        return Response({"status": 400}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(user)
    return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def customer_change_profile(request):
#     # how make a field optional? set a default value or set required = false
#
#     user = request.user
#     customer = Customer.objects.filter(user=user).first()
#     # customer.image = request.data['image']
#     if customer is None:
#         return Response({"status": 400}, status=status.HTTP_400_BAD_REQUEST)
#     serializer = CustomerSerializer(data=request.data)
#     if serializer.is_valid():
#         customer = serializer.update(customer, serializer.validated_data)
#         # customer.image = request.FILES['image']
#         customer.isCompleted = True
#         customer.save()
#         return Response({"status": 200}, status=status.HTTP_200_OK)
#
#     else:
#         # return Response({str(serializer.errors)})
#         return Response({"status": 403}, status=status.HTTP_400_BAD_REQUEST)

# class SignUp(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = LoginUserSerializer(data=data)
#         if serializer.is_valid():
#             print(serializer.data)
#             user = User.object.create_user(password=data['password'], email=data['email'])
#             token, create = Token.objects.get_or_create(user=user)
#             return Response({"token : ": token.key})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # @permission_classes([IsAuthenticated])
# # @api_view(['GET'])
# # def get_users(request):
# #     users = User.objects.filter().by_order('score')
# #     serializer = UserListSerializer(users,many = True)

# @api_view(['POST'])
# def login(request):
#     try:
#         data = request.data
#         password = data['password']
#         email = data['email']
#         user = User.object.filter(email=email).first()

#         print(user)
#         if user.check_password(raw_password=password):
#             token, create = Token.objects.get_or_create(user)
#             return Response(token.key)
#         else:
#             return Response("login failed")
#     except:
#         return Response("invalid data")

