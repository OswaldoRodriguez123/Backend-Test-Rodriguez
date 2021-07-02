from .test_core import CoreTest
from django.urls import reverse
from menu.models import Menu, Food, Option

class MenuTest(CoreTest):

    @classmethod
    def setUp(self):
        super(MenuTest, self).setUp()
        name = 'Rice with hamburger, Salad and Dessert'
        date = "2021-07-02"
        menu = Menu.objects.create(name=name, date=date);
        food = Food.objects.create(name="Rice with hamburger, Salad and Dessert");
        option = Option.objects.create(menu_id=menu.pk,food_id=food.pk)
        self.data = {
            'id': menu.pk,
            'name': name,
            'date': date,
            'employee_document': '26339939-0',
            'employee_name': 'Oswaldo Rodriguez',
            'details': 'no tomatoes in the salad',
            'option_id': option.pk
        }
        self.url_home = reverse('menu_home')
        self.url_add = reverse('menu_add')
        self.url_edit = reverse('menu_edit', kwargs={'id': menu.pk})
        self.url_delete = reverse('menu_delete', kwargs={'id': menu.pk})
        self.url_options = reverse('menu_options', kwargs={'uuid': menu.uuid})
        self.url_send = reverse('menu_delete', kwargs={'id': menu.pk})
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu_home.html')
        
    def test_add(self):
        response_get = self.client.get(self.url_add)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'menu_fields.html')
        
        response_post = self.client.post(self.url_add,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'menu_home.html')
        print('menu_add');
        
    def test_edit(self):
        response_get = self.client.get(self.url_edit)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'menu_fields.html')
        
        response_post = self.client.post(self.url_edit,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'menu_home.html')
        print('menu_edit');
        
    def test_delete(self):
        response_post = self.client.post(self.url_delete, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'menu_home.html')
        print('menu_delete');
        
    def test_options(self):
        response_get = self.client.get(self.url_options)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'order_fields.html')
        
        response_post = self.client.post(self.url_options,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'order_fields.html')
        print('menu_options');
        
    def test_send(self):
        response_post = self.client.post(self.url_send, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'menu_home.html')
        print('menu_send');