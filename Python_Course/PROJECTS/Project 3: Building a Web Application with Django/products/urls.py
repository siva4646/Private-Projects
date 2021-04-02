from django.urls import path
from . import views  # . means current folder


#
# /products/1/new
# /products/new

urlpatterns = [
    path("", views.index)
]