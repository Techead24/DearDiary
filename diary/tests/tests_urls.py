# from turtle import title
# from urllib import response
# from django.test import TestCase
# from django.urls import reverse, resolve
# from diary.views import EUV, ELV,EntryDeleteView, EDV, ECV, About
# from users.views import register, profile
# from django.contrib.auth import views as views
# from diary.models import Entry
# from django.contrib.auth.models import User





# # Create your tests here.


# class TestURLs(TestCase):
    
#     def setup(self):
#         testuser = self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         obj = Entry.objects.create( title = 'test',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
    
#     def test_entrylist(self):
#         url = reverse('entry-list')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, ELV)
        
#     def test_entrycreate(self):
#         url = reverse('entry-create')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, ECV)
    
#     def test_entrydetail(self):
#         self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=self.user)
#         self.post.save()
#         response = reverse('entry-detail', args=[self.post.pk])
#         self.assertEquals(resolve(response).func.view_class, EDV)
        
        
#     def test_entrydelete(self):
#         self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=self.user)
#         url = reverse('entry-delete', args=[self.post.pk])
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, EntryDeleteView)
        
#     def test_entryupdate(self):
#         self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
#         self.post = Entry.objects.create( title = 'test',content = 'testing', date_created = '2022-12-19 09:30', user=self.user)
#         url = reverse('entry-update', args=[self.post.pk])
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, EUV)
    
    
#     def test_about(self):
#         url = reverse('about-page')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func, About)
        
    
#     def test_resgister(self):
#         url = reverse('register')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func, register)
        
        
#     def test_profile(self):
#         url = reverse('profile')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func, profile)
        
    
#     def test_login(self):
#         url = reverse('login')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, views.LoginView)
        
#     def test_logout(self):
#         url = reverse('logout')
#         print(resolve(url)) 
#         self.assertEquals(resolve(url).func.view_class, views.LogoutView)
    
        
    
        
           