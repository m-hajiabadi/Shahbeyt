from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Beyt, Poem,Comment


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        try:
            instance.firstname = validated_data.get('firstname', instance.firstname)
            instance.lastname = validated_data.get('lastname', instance.lastname)
            # todo : email validation required
            instance.email = validated_data.get('email', instance.email)
            instance.image = validated_data.get('image', instance.image)
            #
            instance.username = validated_data.get('username', instance.username)
            instance.bio = validated_data.get('bio', instance.bio)
        except Exception as e:
            raise ValueError (e)
            return False
        instance.save()
        return instance


class UserSerializer_out(serializers.ModelSerializer):
    image = serializers.CharField(source='image.path')
    class Meta:
        model = User
        fields = ('email', 'username', 'bio', 'phone', 'firstname', 'lastname', 'score', 'image', 'id')


class BeytSerializer(serializers.ModelSerializer):
    poem_id = serializers.CharField()

    class Meta:
        model = Beyt
        fields = ('isKing', 'context', 'number_of_beyt', 'poem_id')

    def create(self, validated_data):
        poem_id = validated_data['poem_id']
        poem = Poem.objects.filter(id=poem_id).first()
        if poem is None:
            raise ValueError('poem not exist')
        validated_data.pop('poem_id')
        beyt = Beyt(**validated_data, poem=poem)
        if beyt is None:
            raise ValueError('can not create beyt ')
        beyt.save()
        return beyt


class PoemSerializer_out(serializers.ModelSerializer):
    beyts = serializers.SerializerMethodField()
    creator_name = serializers.CharField(source='creator.username')

    class Meta:
        model = Poem
        fields = ['ghaleb', 'poet', 'beyt_numbers', 'create_data', 'creator_name', 'beyts']

    def get_beyts(self, obj):
        return Beyt.objects.filter(poem_id=obj.id).order_by('number_of_beyt').values('context', 'isKing')


class PoemSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField()

    class Meta:
        model = Poem
        fields = ('user_id', 'poet', 'ghaleb', 'beyt_numbers')

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.object.filter(id=user_id).first()
        poem = Poem(creator=user, **validated_data)
        if poem is None:
            raise ValueError('poem can not create')
        poem.save()
        return poem


class PoemSerializer_test(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = ('poet', 'ghaleb', 'beyt_numbers')


class BeytSerializer_out(serializers.ModelSerializer):
    poem_id = serializers.CharField(source='poem.pk')
    user_id = serializers.CharField(source='poem.creator.id')
    creator_username = serializers.CharField(source='poem.creator.username')
    poem_create_date = serializers.DateField(source='poem.create_data')

    class Meta:
        model = Beyt
        fields = ('isKing', 'context', 'number_of_beyt', 'poem_id', 'user_id', 'creator_username', 'poem_create_date')



class CommentSerializer(serializers.ModelSerializer):
    poem_id = serializers.CharField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('context', 'created_date', 'poem_id','user_id')

    def create(self, validated_data):
        poem_id = validated_data['poem_id']
        poem = Poem.objects.filter(id=poem_id).first()
        if poem is None:
            raise ValueError('poem not exist')
        user_id = validated_data['user_id']
        user = User.object.filter(id=user_id).first()
        if poem is None:
            raise ValueError('user not exist')
        validated_data.pop('user_id')
        comment = Comment(**validated_data, poem=poem,user=user)
        if comment is None:
            raise ValueError('can not create comment ')
        comment.save()
        return comment


class CommentSerializer_out(serializers.ModelSerializer):
    poem_id = serializers.CharField(source='poem.pk')
    user_id = serializers.CharField(source='user.pk')
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Comment
        fields = ('like_number', 'context', 'poem_id', 'user_id','username','dislike_number','created_date')