from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginUserSerializer, serializers
from .models import User
from rest_framework.authtoken.models import Token


class SignUp(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():
            print(serializer.data)
            user = User.object.create_user(password=data['password'], email=data['email'])
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
