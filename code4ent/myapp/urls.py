from django.urls import path
from myapp.views import (
    dynamic_url_view,
    delete_object_view,
    database_list_view
)

app_name = 'myapp'
urlpatterns = [
    path('<int:my_id>/', dynamic_url_view, name='myapp-detail'),
    path('<int:my_id>/delete/', delete_object_view, name='delete'),
    path('my_list/', database_list_view, name='list_items'),
]

