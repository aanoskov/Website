from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.

class Blog(Model):
    title = CharField(max_length=80)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    author = ForeignKey(User, on_delete=CASCADE, default=1)
    opened = BooleanField(default=False)
    def __str__(self):
        return str(self.title)


class Post(Model):
    blog = ForeignKey(Blog, on_delete=CASCADE)
    subject = CharField(max_length=80)
    text = TextField(max_length=4096)
    created_at=  DateTimeField('creation timestamp', auto_now_add=True)
    updated_at = DateTimeField('update timestamp', auto_now=True)

    
    def __str__(self):
        return str(self.subject)

class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE, default=1)
    phone = CharField(max_length=18)
    cost = IntegerField()
