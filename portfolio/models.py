from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    delivery_date = models.DateField()
    project_url = models.URLField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return f'Project : {self.project_name} / URL : {self.project_url}'


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return f'image:{self.image}'


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_image = models.ImageField(upload_to='customers/', blank=True)
    country = CountryField()
    quote = models.TextField()
    review_ranks = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return f'{self.customer_name}'


class Service(models.Model):
    title_service = models.CharField(max_length=200)
    description_service = models.TextField()
    image_service = models.ImageField(upload_to='services', blank=True)

    def __str__(self):
        return self.title_service


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    datetime_message = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Name:{self.name},Message : {self.message[:20]}'
