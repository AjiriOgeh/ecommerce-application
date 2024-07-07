from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializers


class UserCreateSerializers(BaseUserCreateSerializers):
    class Meta(BaseUserCreateSerializers.Meta):
        fields = ['first_name', 'last_name', 'username', 'password', 'phone_number', 'email']
