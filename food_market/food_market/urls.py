
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",include("food_types.urls")),
    path('admin/', admin.site.urls),
]
