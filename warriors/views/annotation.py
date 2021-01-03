from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Poem, User, Beyt, Comment, Annotation
from ..serializers import PoemSerializer_out, PoemSerializer, BeytSerializer, CommentSerializer, CommentSerializer_out, \
    AllPoemSerializer_out, BeytSerializer_out, AnnotationSerializer
import json

# class ShowPeom (APIView):

# def get_peoem_beyts(self,poem_id):
from ..settings import ADD_POEM_SCORE, PAGE_COMMENT_NUMBER


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_annotation(request):
    try:
        data = request.data
        user = request.user
        poem_id = data['poem_id']
        data['user_id'] = user.id
        poem_context = concate_beyts(poem_id)
        new_start = data['start_index']
        new_end = data['end_index']

        starts = Annotation.objects.filter(poem_id=poem_id).values_list('start_index',flat=True)
        if starts is not None:
            starts = list(starts)
        ends = Annotation.objects.filter(poem_id=poem_id).values_list('end_index',flat=True)

        if ends is not None:
            ends = list(ends)
        for i in range(0, len(starts)):
            if not isCorrectRange(starts[i], ends[i], new_start, new_end,len(poem_context)):
                return Response({"status": 4001}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AnnotationSerializer(data = data)
        if serializer.is_valid():
            annotation = serializer.create(serializer.validated_data)
            print(annotation)
            return Response({"status": 4000}, status=status.HTTP_200_OK)
        print(serializer.errors)
    except Exception as e:
        print(e)
        return Response({"status": 4002}, status=status.HTTP_400_BAD_REQUEST)


# @permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_poem_annotation(request,poem_id):
    try:
        annotations = Annotation.objects.filter(poem_id=poem_id)
        if annotations is None :
            return Response( status=status.HTTP_200_OK)
        serializer = AnnotationSerializer(annotations,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e :
        print(e)
        return Response({"status": 4003}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_annotation(request,user_id):
    try:
        annotations = Annotation.objects.filter(user_id = user_id)
        if annotations is None :
            return Response( status=status.HTTP_200_OK)
        serializer = AnnotationSerializer(annotations,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as e :
        print(e)
        return Response({"status": 4003}, status=status.HTTP_400_BAD_REQUEST)


def concate_beyts(poem_id):
    dic = Beyt.objects.filter(poem_id=poem_id).order_by('number_of_beyt').values('context')
    # test = Beyt.objects.filter(poem_id=poem_id).order_by('number_of_beyt').values('context', flat=True)
    # print(list(test))
    poem = ''
    for i in dic:
        poem = poem + i['context'] + '\n'
    poem = remove_last_line_from_string(poem)
    return poem


def isCorrectRange(start, end, new_start, new_end,size):
    if new_end < start:
        if new_start < new_end:
            return True
    if new_start > end:
        if new_end > new_start:
            return True
    return False


def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]
# 3000 : ok
# 3001 :
# 3002 : invalid poem data
# 3003 : poem not exist
# 3005 : invalid comment data
# 3007 : comment not exist
