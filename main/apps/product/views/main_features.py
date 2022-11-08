from rest_framework.generics import ListCreateAPIView, ListAPIView

from ..models.main_features import MainFeatureType,MainFeatureValue
from ..serializers.main_features import (
        MainFeatureValueCreateSerializer,
        MainFeatureTypeCreateSerializer,
        MainFeatureTypeListSerializer,
        MainFeatureValueListSerializer
    )


class MainFeatureTypeCreateView(ListCreateAPIView):

    queryset = MainFeatureType.objects.all()
    serializer_class = MainFeatureTypeCreateSerializer

main_feature_type_view = MainFeatureTypeCreateView.as_view()


class MainFeatureValueCreateView(ListCreateAPIView):

    queryset = MainFeatureValue.objects.all()
    serializer_class = MainFeatureValueCreateSerializer


main_feature_value_view = MainFeatureValueCreateView.as_view()

class MainFeatureTypeListView(ListAPIView):

    queryset = MainFeatureType.objects.all()
    serializer_class = MainFeatureTypeListSerializer

main_feature_type_list_view = MainFeatureTypeListView.as_view()


class MainFeatureValueListView(ListAPIView):

    queryset = MainFeatureValue.objects.all()
    serializer_class = MainFeatureValueListSerializer


main_feature_value_list_view = MainFeatureValueListView.as_view()

