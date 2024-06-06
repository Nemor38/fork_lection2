from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee, Position

class EmployeeProfileViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(name="Test Employee", position="Developer")
        self.url = reverse('employee_profile', kwargs={'pk': self.employee.pk})

    def test_profile_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'employee/profile.html')

    def test_profile_view_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['employee'], self.employee)

class EmployeeDeleteViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(name="Test Employee", position="Developer")
        self.url = reverse('employee_delete', kwargs={'pk': self.employee.pk})

    def test_delete_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'employee/confirm_delete.html')

    def test_delete_employee(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)  # Redirects after deletion
        self.assertFalse(Employee.objects.filter(pk=self.employee.pk).exists())

class EmployeeUpdateViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(name="Test Employee", position="Developer")
        self.url = reverse('employee_update', kwargs={'pk': self.employee.pk})

    def test_update_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'employee/update.html')

    def test_update_employee(self):
        new_data = {
            'name': 'Updated Employee',
            'position': 'Senior Developer'
        }
        response = self.client.post(self.url, new_data)
        self.assertEqual(response.status_code, 302)  # Redirects after update
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.name, 'Updated Employee')
        self.assertEqual(self.employee.position, 'Senior Developer')

class PositionViewSetTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.position = Position.objects.create(title="Developer")

    def test_list_positions(self):
        url = reverse('position-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), Position.objects.count())

    def test_create_position(self):
        url = reverse('position-list')
        data = {
            'title': 'Manager'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Position.objects.count(), 2)
        self.assertEqual(Position.objects.last().title, 'Manager')

    def test_update_position(self):
        url = reverse('position-detail', kwargs={'pk': self.position.pk})
        data = {
            'title': 'Senior Developer'
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.position.refresh_from_db()
        self.assertEqual(self.position.title, 'Senior Developer')

    def test_delete_position(self):
        url = reverse('position-detail', kwargs={'pk': self.position.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Position.objects.filter(pk=self.position.pk).exists())
