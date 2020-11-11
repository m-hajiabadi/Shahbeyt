from django.db import models
from datetime import datetime
from custom.feilds import SeparatedValuesField 

class User(models.Model):
    firstname = models.CharField()
    lastname = models.CharField()
    phone = models.CharField()
    bio = models.CharField()
    image = models.ImageField()
    creation_date = models.DateField()
    favourite = SeparatedValuesField()
    nobugh = models.IntegerField()

    def __str__(self):
        return self.firstname + self.lastname

class Poem(models.Model):   
    poem_id = models.IntegerField(default=0, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    king_beyt = models.IntegerField(default=0)
    creation_date = models.DateField(default=datetime.now())
    context = SeparatedValuesField()

    def __str__(self):
        return self.context
    

class Beyt(models.Model):
    beyt_id = models.IntegerField(default=0, primary_key=True)
    have_explain = models.BooleanField(default=False)
    creation_date = models.DateField(default=datetime.now())
    isking = models.BooleanField(default=False)
    context = models.TextField()

    def __str__(self):
        return self.context
    

class Explain(models.Model):
    explian_id = models.IntegerField(default=0, primary_key=True)
    like_number = models.IntegerField(default=0)
    dislike_number = models.IntegerField(default=0)
    context = models.TextField()

    def __str__(self):
        return self.context
    
