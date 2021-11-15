from rest_framework.test import APITestCase
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from bonds.models import Bond

class HelloWorld(APITestCase):
    def test_root(self):
        
        user = User.objects.create_user('leon')
        user.save()
        user = User.objects.get(username='leon')

        self.client.force_authenticate(user=user)
        resp = self.client.get("/bonds/")

        assert resp.status_code == 200
