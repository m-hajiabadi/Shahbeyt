from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from ..serializers import LoginUserSerializer, serializers, UserSerializer, UserSerializer_out
from ..settings import PROFILE_COMPLETE_SCORE

from ..models import User, Poem
from rest_framework.authtoken.models import Token

from ..serializers import PoemSerializer_out


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    print(user.image.path)
    try :
        if user is None:
            return Response({"status": 2001}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer_out(user)
        return Response(serializer.data)
    except Exception as e:
        print (e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def user_poems(request,user_id):
    try:
        poems = Poem.objects.filter(creator_id = user_id)
        if poems is None:
            return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PoemSerializer_out(poems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e :
        print(e)
        return Response({"status": 3004}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    if user is None:
        return Response({"status": 2001}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data, partial=True)
    print(request.data)
    if serializer.is_valid():
        user = serializer.update(user, serializer.validated_data)
        if not user.isComplete:
            user.score += PROFILE_COMPLETE_SCORE
            user.isComplete = True
            user.save()
    else:
        print("update profile error: " ,serializer.errors)
        return Response({"status": 2002}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"status": 2000}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_profile(request, user_id):
    try:
        user = User.object.filter(pk=user_id).first()
        if user is None:
            return Response({"status": 2003}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer_out(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": 2001}, status=status.HTTP_400_BAD_REQUEST)
