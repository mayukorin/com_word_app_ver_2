from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
# Create your models here.


class UserManager(BaseUserManager):
  def create_user(self, email_field, password_field, **extra_fields):
    if not email_field:
      raise ValueError('メールアドレスは必須です')
    
    user = self.model(
      email=self.normalize_email(email_field), 
      password=password_field,
      **extra_fields
    )
      # username=extra_fields)

    # パスワードのハッシュ化
    user.set_password(password_field)
    
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    user = self.create_user(email, password, **extra_fields)
    user.is_superuser = True
    user.is_staff = True

    user.save(using=self._db)
    return user



class User(AbstractUser):
  
  email = models.EmailField(
        verbose_name='メールアドレス',
        max_length=255,
        unique=True,
    )
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  username = models.CharField(verbose_name='ユーザ名', max_length=150, blank=True)

  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username',]

class StopWord(models.Model):

    class Meta:
        db_table = "stop_word"

    word = models.CharField(verbose_name='ストップワード', max_length=150)