
from rest_framework import serializers

from apps.models.contact_labels import ContactLabels
from apps.models.contacts import Contacts


class ContactLabelSerializer(serializers.ModelSerializer):
    """
        연락처 라벨  Serializer
    """

    class Meta:
        model = ContactLabels
        fields = '__all__'


class ContactLabelListSerializer(serializers.ModelSerializer):
    """
        연락처 라벨 목록  Serializer
    """

    from apps.serializers.label_serializer import LabelListSerializer
    label = LabelListSerializer(
        many=False,
        required=True,
        source=ContactLabels.label_seq.field.name
    )
    class Meta:
        model = ContactLabels
        fields = ['seq', 'label']

