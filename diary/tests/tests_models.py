from django.db import models
from diary.models import Entry
from unittest import TestCase
from django.contrib.auth.models import User



class TestModel(TestCase):
    
    def test_createentry_peruser(self):
        testuser = self.user = User.objects.create_user('max', 'lennon@thebeatles.com', 'password')
        testuser.save()
        obj = Entry.objects.create( title = 'test',content = 'testing',date_created = '2022-12-19 09:30', user = testuser)
        obj.save()
        self.assertEquals(str(obj), 'test')

        