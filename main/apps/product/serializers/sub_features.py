from rest_framework import serializers

from ..models.sub_features import SubFeatureType,SubFeatureValue

class SubFeatureTypeCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = SubFeatureType
        fields = "__all__"


class SubFeatureValueCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubFeatureValue
        fields = "__all__"


class SubFeatureValueListSerializer(serializers.ModelSerializer):
    type = SubFeatureTypeCreateSerializer()
    class Meta:
        model = SubFeatureValue
        fields = "__all__"


class SubFeatureTypeListSerializer(serializers.ModelSerializer):
    values = SubFeatureValueListSerializer
    class Meta:
        model = SubFeatureValue
        fields = "__all__"