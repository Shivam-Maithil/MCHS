from django.db import models
from django.urls import reverse


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    notice_content = models.TextField()

    def __str__(self):
        return self.title


class StudentRegistration(models.Model):
    name = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ResultYear(models.Model):
    year = models.CharField(max_length=10)

    def __str__(self):
        return self.year


class Result10th(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    percentages = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Result12th(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=True)
    percentages = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class EventPicture(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    image = models.ImageField()
    featured = models.BooleanField(blank=True)

    def __str__(self):
        return self.event.title


class Event(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:gallery', kwargs={
            'id': self.id
        })
