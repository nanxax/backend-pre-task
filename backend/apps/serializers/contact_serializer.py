
from rest_framework import serializers

from apps.models.contacts import Contacts

class ContactSerializer(serializers.ModelSerializer):
    """
        연락처  Serializer
    """

    create_by = serializers.CharField(default="admin")
    update_by = serializers.CharField(default="admin")

    class Meta:
        model = Contacts
        fields = '__all__'


class ContactNoneSerializer(serializers.ModelSerializer):
    """
        연락처 None  Serializer
    """

    class Meta:
        model = Contacts
        fields = []


class ContactListSerializer(serializers.ModelSerializer):
    """
        연락처 목록  Serializer
    """
    class Meta:
        model = Contacts
        fields = ['seq', 'image_url', 'name', 'email','phone_number', 'company', 'position']