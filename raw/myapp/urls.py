from django.urls import path
from .views import fbv_view, ProductDetailView, ProductListView
urlpatterns = [
    path('fbv/', fbv_view, name='fbv'),
    path('', ProductDetailView.as_view(), name='detail'),
    path('<int:id>/', ProductDetailView.as_view(), name='detail2'),
    path('list/', ProductListView.as_view(), name='product_list'),
]