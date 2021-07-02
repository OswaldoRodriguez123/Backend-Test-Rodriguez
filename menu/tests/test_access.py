from .test_core import CoreTest

class AccessTest(CoreTest):

    @classmethod
    def setUp(self):
        super(AccessTest, self).setUp()

    def test_login(self):
        self.assertTrue(self.user.is_authenticated) 
        
    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)