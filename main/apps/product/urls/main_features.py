from django.urls import path

from ..views import main_features

urlpatterns = [

    path('create-main-features-type/',view=main_features.main_feature_type_view,name='main_features_type'),
    path('create-main-features-value/',view=main_features.main_feature_value_view,name='main_features_value'),
    path('main-features-type-list/',view=main_features.main_feature_type_list_view,name='main_features_type'),
    path('main-features-value-list/',view=main_features.main_feature_value_list_view,name='main_features_value'),



]