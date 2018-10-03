from django.urls import reverse,resolve
from django.test import TestCase

# class HomeTests(TestCase):
#     def test_home_view_status_code(self):
#         view = resolve('/')
#         response = self.client.get(view)
#         self.assertEquals(response.status_code, 200)

#     def test_home_url_resolves_home_view(self):
#         view = resolve('/')
#         self.assertEquals(view.func, home)