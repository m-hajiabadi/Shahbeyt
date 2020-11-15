from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


# from django.contrib.admin.forms import

# def create_user(self, username, personal, family, email, password=None):
#     """
#     Create and save a normal (not-super) user.
#     """
#     user = self.model(
#         username=username,
#         personal=personal,
#         family=family,
#         email=self.normalize_email(email),
#         is_superuser=False,
#         is_active=True,
#     )
#     user.set_password(password)
#     user.save(using=self._db)
#     return user
#
#
# def create_superuser(self, username, personal, family, email, password):
#     """
#     Create and save a superuser.
#     """
#     user = self.model(
#         username=username,
#         personal=personal,
#         family=family,
#         email=self.normalize_email(email),
#         is_superuser=True,
#         is_active=True,
#     )
#     user.set_password(password)
#     user.save(using=self._db)
#     return user

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_superuser=True,#TODO:this line should change
            # is_staff=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # image = models.ImageField()
    creation_date = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']  # email and password is required by default

    def __str__(self):
        return self.firstname + self.lastname

# class Poem(models.Model):
#     poem_id = models.IntegerField(default=0, primary_key=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     king_beyt = models.IntegerField(default=0)
#     creation_date = models.DateField(default=datetime.now())
#     context = SeparatedValuesField()
#
#     def __str__(self):
#         return self.context
#
# #
# class Beyt(models.Model):
#     beyt_id = models.IntegerField(default=0, primary_key=True)
#     have_explain = models.BooleanField(default=False)
#     creation_date = models.DateField(default=datetime.now())
#     isking = models.BooleanField(default=False)
#     context = models.TextField()
#
#     def __str__(self):
#         return self.context
#
#
# class Explain(models.Model):
#     explian_id = models.IntegerField(default=0, primary_key=True)
#     like_number = models.IntegerField(default=0)
#     dislike_number = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.context
#
