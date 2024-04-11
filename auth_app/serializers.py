from rest_framework import serializers
from .models import AccountModel

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    def create(self, validated_data):
        user = AccountModel.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            mobile=validated_data['mobile'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = AccountModel
        fields = ['name', 'email', 'mobile', 'password']
        extra_kwargs = {
            'email': {'error_messages': {'required': 'Email is required!'}}
        }