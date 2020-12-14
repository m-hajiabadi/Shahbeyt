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
from ..settings import ADD_POEM_SCORE


@api_view(['GET'])
def show_poem(request, poem_id):
    try:
        poem = Poem.objects.filter(pk=poem_id).first()
        if poem is None:
            return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PoemSerializer_out(poem)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def show_all_poem(request):
    # print('salam')
    poem = Poem.objects.all()
    if poem is None:
         return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
    serializer = PoemSerializer_out(poem,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def delete_poem(request,poem_id):
    try:
        poem = Poem.objects.filter(pk=poem_id).first()
        if poem is None:
            return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
        poem.delete()
        return Response( status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"general problem"}, status=status.HTTP_400_BAD_REQUEST)


# except:
#     return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


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

    user.score = user.score + ADD_POEM_SCORE
    user.save()
    return Response({"status": 3000}, status=status.HTTP_200_OK)

# 3000 : ok
# 3001 :
# 3002 : invalid poem data
# 3003 : poem not exist
