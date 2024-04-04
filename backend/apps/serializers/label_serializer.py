
from rest_framework import serializers
from apps.models.labels import Labels


class LabelSerializer(serializers.ModelSerializer):
    """
        라벨  Serializer
    """

    class Meta:
        model = Labels
        fields = '__all__'


class LabelListSerializer(serializers.ModelSerializer):
    """
        라벨 목록 Serializer
    """

    class Meta:
        model = Labels
        fields = '__all__'