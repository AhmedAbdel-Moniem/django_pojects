from django.urls import path
from .views import fbv_view, CBV, DetailView, ListView, CreateView

urlpatterns = [
    path('rawcreate/', CreateView.as_view(), name='raw_form'),
    path('rawlist', ListView.as_view(), name='rawlist'),
    path('<int:id>/', DetailView.as_view(), name='detail'),
    path('fbv/', fbv_view, name='fbv'),
    path('cbv/', CBV.as_view(), name='cbv'),
]
