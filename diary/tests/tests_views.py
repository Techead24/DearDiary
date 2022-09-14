# # from multiprocessing.connection import Client
# from datetime import date
# from distutils.core import setup
# from unittest import TestCase
# from urllib import response
# from django.test import TestCase, Client
# from django.urls import reverse
# from django.contrib.auth.models import User
# from diary.models import  Entry
# import json




# # Create your tests here.

# class TestViews(TestCase):
    
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')

#     #LOGIN
#     def test_login_GET(self):
#         response=self.client.get(reverse('login'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/login.html')
        
        
#     def test_login_POST(self):
#         self.user = User.objects.create_user('ronaldo', 'cr7@gmail.com', 'suiii191')
#         self.person = Client()
#         url = reverse('login')
#         response=self.client.post(url, {'username':'ronaldo', 'password':'suiii191'})
#         self.assertEquals(response.status_code, 302)   
        
    
    
    
#     #LOGOUT
#     def test_logout_GET(self):
#         response=self.client.get(reverse('logout'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/logout.html')
        
    
    
    
#     #ENTRY LIST
#     def test_entrylist_GET(self):
#         self.person = Client()
#         self.user = User.objects.create_user('ronaldo', 'cr7@gmail.com', 'suiii191')
#         self.user.save()
#         self.client.login(username='ronaldo', password='suiii191')
#         response=self.client.get(reverse('entry-list'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'entries\entry_list.html')
    
    
    
#     #ENTRY DETAIL - FOREIGN KEY USED
#     def test_entrydetail_GET(self):
#         self.client = Client()
#         testuser = User.objects.create_user('linda', 'linda@gmail.com', 'champagne191')
#         testuser.save()
#         self.client.login(username = 'linda', password = 'champagne191')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=testuser)
#         self.url = reverse('entry-detail', args = [self.post.pk] )
#         response = self.client.get(self.url)
#         self.assertEquals(response.status_code, 200)
    
    
    
    
    
    
    
#     # ENTRY UPDATE - FOREAIGN KEY USED
#     def test_entryupdate_GET(self):
#         self.client = Client()
#         testuser = User.objects.create_user('sarah', 'sarah@gmail.com', 'manchester191')
#         testuser.save()
#         self.client.login(username = 'sarah', password = 'manchester191')
#         self.post =Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
#         self.url = reverse('entry-update', args = [self.post.pk])
#         response = self.client.get(self.url)
#         self.assertEquals(response.status_code, 200)

        
    
    
#     def test_entryupdate_GET(self):
#         self.client = Client()
#         testuser = User.objects.create_user('sarah', 'sarah@gmail.com', 'manchester191')
#         testuser.save()
#         self.client.login(username = 'sarah', password = 'manchester191')
#         self.post =Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
#         self.url = reverse('entry-update', args = [self.post.pk])
#         response = self.client.get(self.url)
#         self.assertEquals(response.status_code, 200)

    
    
#     def test_entryupdate_POST(self):
#         self.client = Client()
#         testuser = User.objects.create_user('sarah', 'sarah@gmail.com', 'manchester191')
#         testuser.save()
#         self.client.login(username = 'sarah', password = 'manchester191')
#         self.post =Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
#         self.post.save()
#         self.url = self.client.post(reverse('entry-update', args = [self.post.pk]), {'title' :'test2', 'content' : 'update test'})
#         self.assertEquals(self.url.status_code, 302)
    
    
    
    
    
     
#     # ENTRY DELETE - FOREIGN KEY USED
#     def test_entrydelete_GET(self):
#         self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=self.user)
#         self.user.save()
#         self.post.save()
#         self.client.login(username = 'max', password = 'password')
#         url = reverse('entry-delete', args=[self.post.pk])
#         response = self.client.get(url)
#         self.assertEquals(response.status_code, 200)
        
    
    
    
#     def test_entrydelete_POST(self):
#         self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=self.user)
#         self.user.save()
#         self.post.save()
#         url = reverse('entry-delete', args=[self.post.pk])
#         self.client.login(username='max', password='password')
#         response = self.client.delete(url)
#         self.assertEquals(response.status_code, 302)
    
    
    
    
    
    
#     #ENTRY CREATE
#     def test_entrycreate_GET(self):
#         self.client = Client()
#         self.user = User.objects.create_user('jane', 'janey@gmail.com', 'password191')
#         self.user.save()
#         self.client.login(username='jane', password='password191')
#         response= self.client.get(reverse('entry-create'))
#         self.assertEquals(response.status_code, 200)
    
    
    
    
#     def test_entrycreate_POST(self):
#         testuser = self.user = User.objects.create_user('linda', 'linda@gmail.com', 'password2')
#         testuser.save()
#         obj = Entry.objects.create( title = 'test1',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
#         obj.save()
#         self.client.login(username='linda', password='password2')
#         response=self.client.post(reverse('entry-create'), {
#             'title' : 'test1',
#             'content':'testing',
#             'date_created':'2022-12-19 09:30'
#         })
#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(Entry.objects.filter(title = 'test1', content = 'testing').count(), 2)
        
        
        
        
        
#     #REGISTER
#     def test_registeruser_GET(self):
#         response=self.client.get(reverse('register'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/register.html')
        
        
#     def test_registeruser_POST(self):
#         self.user = {
#             'username':'uche',
#             'email': 'uche@uche.com',
#             'password1':'pasta191',
#             'password2':'pasta191'
#             }
#         response = self.client.post(reverse('register'), self.user)
#         self.assertEquals(response.status_code, 302)
        
    