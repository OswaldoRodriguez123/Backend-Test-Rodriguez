from .test_core import CoreTest
from django.urls import reverse
from menu.models import Menu, Food, Option

class OptionTest(CoreTest):

    @classmethod
    def setUp(self):
        super(OptionTest, self).setUp()
        menu = Menu.objects.create(name="Today's menu", date="2021-07-02");
        food = Food.objects.create(name="Rice with hamburger, Salad and Dessert");
        option = Option.objects.create(menu_id=menu.pk,food_id=food.pk)
        self.data = {
            'id': option.pk,
            'food_id': food.pk
        }        
        self.url_home = reverse('option_home', kwargs={'menu_id': menu.pk})
        self.url_add = reverse('option_add', kwargs={'menu_id': menu.pk})
        self.url_edit = reverse('option_edit', kwargs={'id': option.pk})
        self.url_delete = reverse('option_delete', kwargs={'id': option.pk})
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'option_home.html')
        
    def test_add(self):
        response_get = self.client.get(self.url_add)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'option_fields.html')
        
        response_post = self.client.post(self.url_add,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'option_home.html')
        print('option_add');
        
    def test_edit(self):
        response_get = self.client.get(self.url_edit)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'option_fields.html')
        
        response_post = self.client.post(self.url_edit,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'option_home.html')
        print('option_edit');
        
    def test_delete(self):
        response_post = self.client.post(self.url_delete, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'option_home.html')
        print('option_delete');