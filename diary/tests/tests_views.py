# from multiprocessing.connection import Client
from datetime import date
from distutils.core import setup
from unittest import TestCase
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from diary.models import  Entry
import json




# Create your tests here.

class TestViews(TestCase):
    
    def setUp(self):
            self.client = Client()
            self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')

    #LOGIN
    def test_login_GET(self):
        self.client.login(username='john', password='password')
        response=self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        
        
    def test_login_POST(self):
        self.user = {
            'username':'max',
            'name':'max imum',
            'password':'password'
        }
        self.client.post(reverse('login'), self.user)
        user = User.objects.filter(username=self.user['username']).first()
        TU = User.objects.create_user('johnny', 'lennony@thebeatles.com', 'passwordy')

        # user.is_active=True
        TU.is_active = True
        # self.user.save()
        self.client.login(username=self.user['username'], password=self.user['password'])
        response=self.client.post(reverse('login'),self.user)
        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'users/login.html')
        
    
    
    
    #LOGOUT
    def test_logout_GET(self):
        self.client.login(username='max', password='password')
        response=self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/logout.html')
        
        
    # def test_logout_POST(self):
    #     self.client.login(username='max', password='password')
    #     response=self.client.post(reverse('logout'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'users/logout.html')
    
    
    
    
    #ENTRY LIST
    # def test_entrylist_GET(self):
    #     # self.user.save()
    #     self.client.login(username='max', password='password')
    #     response=self.client.get(reverse('entry-list'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'entries\entry_list.html')
    
    
    # def test_entrylist_POST(self):
    #     testuser = self.user = User.objects.create_user('linda', 'linda@gmail.com', 'password2')
    #     testuser.save()
    #     obj = Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
    #     obj.save()
    #     self.client.login(username='linda', password='password2')
    #     response=self.client.post(reverse('entry-create'), {
    #         'title' : 'test1',
    #         'content':'testing',
    #         'date_created':'2022-12-19 09:30'
    #     })
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(Entry.objects.filter(title = 'test1', content = 'testing').count(), 2)
    
    
    
    #ENTRY DETAIL - FOREAIGN KEY USED
    
    
    
    
    
    
    
    
    
    
    #ENTRY UPDATE - FOREAIGN KEY USED
    
    
    
    
    
    
    
    #ENTRY DELETE - FOREAIGN KEY USED
    # def test_entrylist_GET(self):
    #     self.client.login(username='max', password='password')
    #     response=self.client.get(reverse('entry-delete'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'entries\entry_delete.html')
    
    
    
    
    
    
    
    
    
    #ENTRY CREATE
    # def test_entrycreate_GET(self):
        
    #     self.client.login(username='max', password='password')
    #     response=self.client.get(reverse('entry-create'))
    #     self.assertEquals(response.status_code, 302)
    #     # self.assertTemplateUsed(response, 'entries\entry_form.html')
    
    
    def test_entrycreate_POST(self):
        testuser = self.user = User.objects.create_user('linda', 'linda@gmail.com', 'password2')
        testuser.save()
        obj = Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
        obj.save()
        self.client.login(username='linda', password='password2')
        response=self.client.post(reverse('entry-create'), {
            'title' : 'test1',
            'content':'testing',
            'date_created':'2022-12-19 09:30'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Entry.objects.filter(title = 'test1', content = 'testing').count(), 2)
        
        
    # def test_entrycreate_POST(self):
    #     self.form_data = {
    #         'title' : 'test1',
    #         'content':'testing',
    #         }
        
    #     form = ECV(data=self.form_data)
    #     self.assertTrue(super(form.form_valid(form)))
    #     obj = form.save()
    #     self.assertEqual(obj.title, self.valid_data['title'])