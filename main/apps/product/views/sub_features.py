from rest_framework.generics import ListCreateAPIView, ListAPIView

from ..models.sub_features import SubFeatureType,SubFeatureValue
from ..serializers.sub_features import SubFeatureTypeCreateSerializer, SubFeatureValueCreateSerializer, \
    SubFeatureValueListSerializer, SubFeatureTypeListSerializer


class SubFeatureTypeCreateView(ListCreateAPIView):

    queryset = SubFeatureType.objects.all()
    serializer_class = SubFeatureTypeCreateSerializer

sub_feature_type_view = SubFeatureTypeCreateView.as_view()


class SubFeatureValueCreateView(ListCreateAPIView):

    queryset = SubFeatureValue.objects.all()
    serializer_class = SubFeatureValueCreateSerializer


sub_feature_value_view = SubFeatureValueCreateView.as_view()

class SubFeatureTypeListView(ListAPIView):

    queryset = SubFeatureType.objects.all()
    serializer_class = SubFeatureTypeListSerializer

sub_feature_type_list_view = SubFeatureTypeListView.as_view()


class SubFeatureValueListView(ListAPIView):

    queryset = SubFeatureValue.objects.all()
    serializer_class = SubFeatureValueListSerializer


sub_feature_value_list_view = SubFeatureValueListView.as_view()

