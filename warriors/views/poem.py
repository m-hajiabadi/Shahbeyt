from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Poem, User, Beyt, Comment
from ..serializers import PoemSerializer_out


# class ShowPeom (APIView):

# def get_peoem_beyts(self,poem_id):
@api_view(['GET'])
def show_poem( request, poem_id):
    try :
        poem = Poem.objects.filter(pk=poem_id).first()
        serializer = PoemSerializer_out(poem)
        return Response(serializer.data,status= status.HTTP_200_OK)
    except :
        return Response({"status": 3001})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_poem(reqeust):


