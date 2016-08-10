from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Vehicle(models.Model):
    type_of_vehicle = models.CharField(max_length=20)
    detail_of_vehicle = models.ImageField(upload_to=upload_location,
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.type_of_vehicle


class Location(models.Model):
    location = models.CharField(max_length= 20)
    def __str__(self):
        return self.location


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    vehicle = models.ForeignKey(Vehicle)
    price = models.CharField(max_length=20)
    # 지도 필드
    # 캘린더 필드

    content = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:lend_detail", kwargs={"lend_id":self.id})

    def __str__(self):
        return self.title


