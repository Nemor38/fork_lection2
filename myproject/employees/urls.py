from django.urls import path
from .views import EmployeeProfileView, EmployeeDeleteView, EmployeeUpdateView

urlpatterns = [
    path('employee/<int:pk>/', EmployeeProfileView.as_view(), name='employee_profile'),
    path('employee/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
]
