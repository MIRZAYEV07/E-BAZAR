from rest_framework import serializers

from ..models.main_features import MainFeatureType,MainFeatureValue


class MainFeatureTypeCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = MainFeatureType
        fields = "__all__"


class MainFeatureValueCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainFeatureValue
        fields = "__all__"


class MainFeatureValueListSerializer(serializers.ModelSerializer):
    type = MainFeatureTypeCreateSerializer()
    class Meta:
        model = MainFeatureValue
        fields = "__all__"


class MainFeatureTypeListSerializer(serializers.ModelSerializer):
    values = MainFeatureValueCreateSerializer
    class Meta:
        model = MainFeatureType
        fields = "__all__"