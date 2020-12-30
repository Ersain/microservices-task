from django.urls import path
from .views import PositionViewDetail, PositionViewList

urlpatterns = [
    path('', PositionViewList.as_view(), name='position-list'),
    path('<int:pk>/', PositionViewDetail.as_view(), name='position-detail'),
]
