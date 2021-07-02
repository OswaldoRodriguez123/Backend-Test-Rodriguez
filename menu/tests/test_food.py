from .test_core import CoreTest
from django.urls import reverse
from menu.models import Food

class FoodTest(CoreTest):

    @classmethod
    def setUp(self):
        super(FoodTest, self).setUp()
        name = 'Rice with hamburger, Salad and Dessert'
        food = Food.objects.create(name=name)
        self.data = {
            'id': food.pk,
            'name': name
        }
        self.url_home = reverse('food_home')
        self.url_add = reverse('food_add')
        self.url_edit = reverse('food_edit', kwargs={'id': self.data['id']})
        self.url_delete = reverse('food_delete', kwargs={'id': self.data['id']})
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'food_home.html')
        
    def test_add(self):
        response_get = self.client.get(self.url_add)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'food_fields.html')
        
        response_post = self.client.post(self.url_add,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'food_home.html')
        print('food_add');
        
    def test_edit(self):
        response_get = self.client.get(self.url_edit)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'food_fields.html')
        
        response_post = self.client.post(self.url_edit,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'food_home.html')
        print('food_edit');
        
    def test_delete(self):  
        response_post = self.client.post(self.url_delete, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'food_home.html')
        print('food_delete');