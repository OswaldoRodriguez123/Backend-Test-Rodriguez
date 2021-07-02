from django.db import models
import uuid

class Menu(models.Model):
    
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False)
    uuid = models.UUIDField(primary_key = False, default = uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return self.id
    
class Food(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Foods"

    def __str__(self):
        return self.name
    
class Option(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    menu = models.ForeignKey(Menu, default=1, verbose_name="Menu", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, default=1, verbose_name="Food", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Options"
    
class Order(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    employee_document = models.CharField(max_length=200)
    employee_name = models.CharField(max_length=200)
    option = models.ForeignKey(Option, default=1, verbose_name="Option", on_delete=models.CASCADE)
    details = models.CharField(max_length=200, null=True, blank=True)
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.id