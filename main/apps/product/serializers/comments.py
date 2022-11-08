from rest_framework import serializers

from main.apps.account.serializers.user import UserSerializer
from ..models.comments import Comments


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = "__all__"

class CommentListSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    
    class Meta:
        model = Comments
        fields = "__all__"