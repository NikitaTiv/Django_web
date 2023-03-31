from django.urls import path

from cats.views import index, index_num

urlpatterns = [
    path('cats/', index, name='home'),
    path('cats/<int:catid>/', index_num),
]
