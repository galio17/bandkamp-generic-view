from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']
        read_only_fields=['is_superuser']
        extra_kwargs = {
            'username': {
                'validators': [UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                )],
            },
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all())],
            },
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)