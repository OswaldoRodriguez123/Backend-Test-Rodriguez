from django.test import Client, TransactionTestCase, TestCase, LiveServerTestCase
from django.contrib.auth.models import User

class CoreTest(TransactionTestCase):
    @classmethod
    def setUp(self):
        self.data = {
            'username': 'nora',
            'password': '1234'
        }
        self.user = User.objects.create(username=self.data['username'])
        self.user.set_password(self.data['password'])
        self.user.is_staff = True
        self.user.save()
        self.client = Client()
        self.client.login(username=self.data['username'], password=self.data['password'])
        # self.client.force_login(self.user)