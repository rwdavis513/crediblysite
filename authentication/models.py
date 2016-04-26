from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
   def create_user(self, email, password=None, **kwargs):
      if not email:
          raise ValueError('Users must have a valid email address.')
      if not kwargs.get('username'):
          raise ValueError('Users must have a valid username.')

      account = self.model(email=self.normalize_email(email),username=kwargs.get('username').lower())
      
      account.set_password(password)
      account.save()

      return account
   def create_superuser(self, email, password, **kwargs):
      account = self.create_user(email, password, **kwargs)
      
      account.is_admin = True
      account.save()

      return account


class Account(AbstractBaseUser):
   email = models.EmailField(unique=True)
   username = models.CharField(max_length=40, unique=True)
   
   first_name = models.CharField(max_length=40, blank=True)
   last_name = models.CharField(max_length=40, blank=True)
   tagline = models.CharField(max_length=140, blank=True)

   job_title = models.CharField(max_length=200,blank=True)

   twitter_handle = models.CharField(max_length=20, blank=True)
   facebook_username = models.CharField(max_length=50, blank=True)
   linkedin_username = models.CharField(max_length=50, blank=True)
   google_username = models.CharField(max_length=50, blank=True)
   instagram_username = models.CharField(max_length=50, blank=True)
   pintrest_username = models.CharField(max_length=50, blank=True)

   personal_website = models.URLField(blank=True)

   address_street = models.CharField(max_length=100, blank=True)
   address_city = models.CharField(max_length=100, blank=True)
   address_state = models.CharField(max_length=2, blank=True)
   address_country = models.CharField(max_length=100, blank=True)


   # FileField(upload_to=None, max_length=100, **options)
   #https://docs.djangoproject.com/en/1.8/ref/models/fields/
   #profile_image = models.ImageField(upload_to='/static/media/images/', height_field=None, width_field=None, max_length=150, blank=True)

   is_admin = models.BooleanField(default=False)

   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   objects = AccountManager()

   USERNAME_FIELD = 'email'
   # UUIDField(**options)
   REQUIRED_FIELDS = ['username']

   def __unicode__(self):
       return self.email

   def get_full_name(self):
       if self.first_name != '' or self.last_name != '':
           full_name = ' '.join([self.first_name, self.last_name])
       else:
           full_name = None
       return full_name

   def get_short_name(self):
       return self.first_name

class UserImage(models.Model):

   owner = models.ForeignKey(Account, related_name='image')
   image = models.ImageField(upload_to='static/media/images',max_length=300)
   label = models.CharField(max_length=100, blank=True)
