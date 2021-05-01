from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'email',
                  'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        _email = attrs.get('email', None)
        if _email and User.objects.filter(email=_email).exists():
            raise serializers.ValidationError(
                {'email': ('Um usuário com este email já existe.')})

        return super().validate(attrs)

    def create(self, validated_data):
        # return super().create(validated_data)
        return User.objects.create_user(**validated_data)
