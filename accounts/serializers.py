from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'nickname', 'birth', 'purpose'
        )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            birth=validated_data['birth'],
            purpose=validated_data['purpose']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError()
        
        user = User.objects.get(username=username)

        if not user.check_password(password):
            raise serializers.ValidationError()
        else:
            token = RefreshToken.for_user(user)
            refresh = str(token)
            access = str(token.access_token)

            return {
                'id' : user.id,
                'username' : user.username,
                'access' : access,                    'refresh' : refresh
            }