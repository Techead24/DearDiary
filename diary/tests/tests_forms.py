from django.db import models
from diary.models import Entry
from unittest import TestCase
from django.contrib.auth.models import User
from users.forms import UserRegister
from django.contrib.auth.forms import  UserCreationForm




class TestModel(TestCase):
    
    def test_createuser(self):
        testuser = self.user = User.objects.create_user(username = 'maxine', email = 'maxine@gmail.com', password = 'password1')
        testuser.save()
        self.assertEquals(str(testuser), 'maxine')

        