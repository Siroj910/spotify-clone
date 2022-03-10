from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

get_schema = get_schema_view(
    open.info(	
        title="music application rest api",

    )
)

urlpatterns = [
    path('_admin/', admin.site.urls),
    path('', include('music.urls'))
]
