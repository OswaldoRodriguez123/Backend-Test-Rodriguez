# Generated by Django 3.2.4 on 2021-06-29 03:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Foods',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.food', verbose_name='Food')),
                ('menu', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.menu', verbose_name='Menu')),
            ],
            options={
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('employee_document', models.CharField(max_length=200)),
                ('employee_name', models.CharField(max_length=200)),
                ('details', models.CharField(blank=True, max_length=200, null=True)),
                ('viewed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('option', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.option', verbose_name='Option')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
