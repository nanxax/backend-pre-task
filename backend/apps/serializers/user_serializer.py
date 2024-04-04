
from rest_framework import serializers
from apps.models.users import Users
from apps.serializers.label_serializer import LabelSerializer


class UserSerializer(serializers.ModelSerializer):
    """
        사용자  Serializer
    """
    create_by = serializers.CharField(default="admin")
    update_by = serializers.CharField(default="admin")

    class Meta:
        model = Users
        fields = '__all__'


class UserNoneSerializer(serializers.ModelSerializer):
    """
        사용자 None Serializer
    """

    class Meta:
        model = Users
        fields = []