from django.contrib import admin
from django.urls import path, include
from myapp.views import (
        my_main_page,
        about_page,
        myform_view,
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_main_page, name='home'),
    path('about/', about_page, name='about'),
    path('create_form/', myform_view, name='create_form'),
    path('myapp/', include('myapp.urls')),
    path('blog/', include('blog.urls')),
    # path('create_form2/', render_initial_data, name='create_form2'),
    # courses app
    path('courses/', include('courses.urls')),

    # Raw
    path('raws/', include('raws.urls'),),

    # API
    path('api/', include('myapi.urls')),
    path('api-auth/', include('rest_framework.urls'))

]
