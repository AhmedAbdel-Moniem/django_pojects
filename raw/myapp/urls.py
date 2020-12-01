from django.urls import path
from .views import fbv_view, From_Fbv_2_Cbv
urlpatterns = [
    path('fbv/', fbv_view, name='fbv'),
    path('cbv/', From_Fbv_2_Cbv.as_view(), name='cbv'),
]