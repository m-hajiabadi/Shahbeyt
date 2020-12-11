from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Poem, User, Beyt, Comment
from ..serializers import PoemSerializer_out, PoemSerializer, BeytSerializer
import json


# class ShowPeom (APIView):

# def get_peoem_beyts(self,poem_id):
@api_view(['GET'])
def show_poem(request, poem_id):
    try:
        poem = Poem.objects.filter(pk=poem_id).first()
        serializer = PoemSerializer_out(poem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": 3001})


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_poem(request):
    data = request.data
    user = request.user
    beyts = data.pop('beyts')
    data['user_id'] = user.id
    serializer = PoemSerializer(data=data)
    if serializer.is_valid():
        print(serializer.validated_data)
        poem = serializer.create(serializer.validated_data)
        for cnt, beyt in enumerate(beyts):
            data = {**data, **beyt}
            data['poem_id'] = poem.id
            data['number_of_beyt'] = cnt
            print(data)
            serializer = BeytSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                _ = serializer.create(validated_data=serializer.validated_data)
    else:
        return Response({"status": 3002}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"status": 3000}, status=status.HTTP_200_OK)
