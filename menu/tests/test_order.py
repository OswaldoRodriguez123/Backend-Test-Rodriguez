from .test_core import CoreTest
from django.urls import reverse
from menu.models import Menu, Food, Option, Order

class OptionTest(CoreTest):

    @classmethod
    def setUp(self):
        super(OptionTest, self).setUp()
        menu = Menu.objects.create(name="Today's menu", date="2021-07-02");
        food = Food.objects.create(name="Rice with hamburger, Salad and Dessert");
        option = Option.objects.create(menu_id=menu.pk,food_id=food.pk)
        employee_document = '26339939-0'
        employee_name = 'Oswaldo Rodriguez'
        details = 'no tomatoes in the salad'
        order = Order.objects.create(
            employee_document=employee_document,
            employee_name=employee_name,
            details=details,
            option_id=option.pk
        )
        self.data = {
            'employee_document': employee_document,
            'employee_name': employee_name,
            'details': details,
            'option_id': option.pk
        }
        self.url_home = reverse('order_home')
        self.url_edit = reverse('order_edit', kwargs={'id': order.pk})
        self.url_delete = reverse('order_delete', kwargs={'id': order.pk})
        self.url_view = reverse('order_view', kwargs={'id': order.pk})
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'order_home.html')

    def test_edit(self):
        response_get = self.client.get(self.url_edit)
        self.assertEqual(response_get.status_code, 200)
        self.assertTemplateUsed(response_get, 'order_fields.html')
        
        response_post = self.client.post(self.url_edit,data=self.data, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'order_home.html')
        print('order_edit');
        
    def test_delete(self):
        response_post = self.client.post(self.url_delete, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'order_home.html')
        print('order_delete');
        
    def test_view(self):
        response_post = self.client.post(self.url_view, data={'viewed': True}, follow=True)
        self.assertEqual(response_post.status_code, 200)
        self.assertTemplateUsed(response_post, 'order_home.html')
        print('order_view');