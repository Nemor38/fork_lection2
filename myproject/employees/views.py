from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, UpdateView
from .models import Employee

class EmployeeProfileView(DetailView):
    model = Employee
    template_name = 'employee/profile.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/confirm_delete.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'position']
    template_name = 'employee/update.html'
    success_url = reverse_lazy('employee_list')
