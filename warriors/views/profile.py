from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from  warriors.serializers import LoginUserSerializer, serializers, UserSerializer, UserSerializer_out
from warriors.settings import PROFILE_COMPLETE_SCORE

from warriors.models import User
from rest_framework.authtoken.models import Token



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    if user is None:
        return Response({"status": 2001}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer_out(user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    if user is None:
        return Response({"status": 2001}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data,partial=True)
    if serializer.is_valid():
        user = serializer.update(user, serializer.validated_data)
        if not user.isComplete:
            user.score += PROFILE_COMPLETE_SCORE
            user.isComplete = True
            user.save()
    else :
        return Response({"status": 2002}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"status": 2000}, status=status.HTTP_200_OK)

