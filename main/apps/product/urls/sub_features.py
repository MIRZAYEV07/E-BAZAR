from django.urls import path

from ..views import sub_features

urlpatterns = [

    path('create-sub-features-type/',view=sub_features.sub_feature_type_view,name='sub_features_type'),
    path('create-sub-features-value/',view=sub_features.sub_feature_value_view,name='sub_features_value'),
    path('sub-features-type-list/',view=sub_features.sub_feature_type_list_view,name='sub_features_type'),
    path('sub-features-value-list/',view=sub_features.sub_feature_value_list_view,name='sub_features_value'),



]