from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Poem, User, Beyt, Comment
from ..serializers import PoemSerializer_out, PoemSerializer, BeytSerializer, CommentSerializer, CommentSerializer_out, \
    AllPoemSerializer_out, BeytSerializer_out
import json

# class ShowPeom (APIView):

# def get_peoem_beyts(self,poem_id):
from ..settings import ADD_POEM_SCORE, PAGE_COMMENT_NUMBER


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
    serializer = AllPoemSerializer_out(poem, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


def delete_poem(request, poem_id):
    try:
        poem = Poem.objects.filter(pk=poem_id).first()
        if poem is None:
            return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
        print(poem)
        poem.delete()
        return Response({"status": 3000}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)


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
            if data.get('isKing'):
                data.pop('isKing')
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


@permission_classes([IsAuthenticated])
@api_view(['POST'])
def add_comment(request):
    data = request.data
    user = request.user
    data['user_id'] = user.id
    print(data)
    try:
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            comment = serializer.create(validated_data=serializer.validated_data)
            print('comment created : ', comment)
            return Response({"status": 3000}, status=status.HTTP_200_OK)
        return Response({"status": 3005}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_comment(request, poem_id, offset=0):
    data = request.data
    comments = Comment.objects.filter(poem_id=poem_id)
    if comments is None:
        return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CommentSerializer_out(comments, many=True)
    # TODO : add offset
    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def like_or_dislike_comment(request, comment_id, isLike):
    user = request.user
    try:
        comment = Comment.objects.filter(id=comment_id).first()
        if comment is None:
            return Response({"status": 3007}, status=status.HTTP_400_BAD_REQUEST)
        if comment.liked_user.filter(id=user.id):
            comment.liked_user.remove(user)
        if comment.disliked_user.filter(id=user.id):
            comment.disliked_user.remove(user)
        if isLike:
            comment.liked_user.add(user)
        else:
            comment.disliked_user.add(user)
        return Response({"status": 3000}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def like_poem(request, poem_id):
    try:
        user = request.user
        poem = Poem.objects.filter(id=poem_id).first()
        if poem is None:
            return Response({"status": 3009}, status=status.HTTP_400_BAD_REQUEST)
        poem.liked_users.add(user)
        return Response({"status": 3000}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def remove_like_poem(request, poem_id):
    user = request.user
    try:
        poem = Poem.objects.filter(id=poem_id).first()
        if poem is None:
            return Response({"status": 3003}, status=status.HTTP_400_BAD_REQUEST)
        if poem.liked_users.filter(id=user.id):
            poem.liked_users.remove(user)
        return Response({"status": 3000}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_beyts(request):
    try:
        key = request.GET['key']
        print("this is key of search : ", key)
        beyts = Beyt.objects.filter(context__contains=key)
        serializer = BeytSerializer_out(beyts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({"status": 3001}, status=status.HTTP_400_BAD_REQUEST)

# 3000 : ok
# 3001 :
# 3002 : invalid poem data
# 3003 : poem not exist
# 3005 : invalid comment data
# 3007 : comment not exist
