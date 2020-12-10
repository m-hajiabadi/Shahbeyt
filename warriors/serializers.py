from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Beyt, Poem


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
            # instance.image = validated_data.get('image',instance.image)
            # todo: username validation required
            instance.username = validated_data.get('username', instance.username)
            instance.bio = validated_data.get('bio', instance.bio)
            instance.phone = validated_data.get('phone', instance.phone)
            # todo: password need to encrypt
            instance.password = validated_data.get('password', instance.password)
        except:
            return False
        instance.save()
        return instance


class UserSerializer_out(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'bio', 'phone', 'firstname', 'lastname', 'score')


class PoemSerializer_out(serializers.ModelSerializer):
    beyts = serializers.SerializerMethodField()

    class Meta:
        model = Poem
        fields = '__all__'

    def get_beyts(self, obj):
        return Beyt.objects.filter(poem_id=obj.id).order_by('number_of_beyt').values('context')
