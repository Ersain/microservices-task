from django.urls import path
from .views import EmployeeViewList, EmployeeViewDetail, DepartmentViewList, DepartmentViewDetail

urlpatterns = [
    path('', EmployeeViewList.as_view(), name='employee-list'),
    path('<int:pk>/', EmployeeViewDetail.as_view(), name='employee-detail'),
    path('departments/', DepartmentViewList.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentViewDetail.as_view(), name='department-detail'),
]
