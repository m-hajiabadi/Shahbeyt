from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            is_superuser=False,  # TODO:this line should change
            # is_staff=True
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_staff = True
        user.admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username):
        """
        Creates and saves a superuser with the given email and password.
        """
        # user = self.create_user(
        #     email=email,
        #     password=password,
        # )
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_superuser=True,  # TODO:this line should change
            # is_staff=True
        )
        user.is_staff = True
        user.admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    creation_date = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    isComplete = models.BooleanField(default=False)
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'username']  # email and password is required by default

    def __str__(self):
        return self.firstname + self.lastname

class Poem(models.Model):
    GHALEB_LIST = ['رباعی', 'مثنوی', 'غزل', 'قصیده']
    GHALEB_CHOISES = [(number, name) for number, name in enumerate(GHALEB_LIST)]
    liked_users = models.ManyToManyField(to =User,related_name='liked_poems')

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    poet = models.CharField(max_length=200)
    beyt_numbers = models.IntegerField()
    create_data = models.DateField(auto_now_add=True)
    ghaleb = models.CharField(max_length=50)




class Beyt(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    context = models.TextField()
    isKing = models.BooleanField(default=False)
    number_of_beyt = models.IntegerField()


class Comment(models.Model):
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    context = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_user = models.ManyToManyField(User,related_name='liked_comments')
    disliked_user=models.ManyToManyField(User,related_name='disliked_comments')

class Annotation(models.Model):
    context = models.TextField()
    date = models.DateField(auto_now_add=True)
    poem = models.ForeignKey(Poem,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_index = models.IntegerField()
    end_index = models.IntegerField()


