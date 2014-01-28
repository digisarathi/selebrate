from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.name
    

class EventType(models.Model):
    name = models.CharField(max_length=20)
    
    
    def __unicode__(self):
        return self.name

class ServiceType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    eventDate = models.DateField()
    typeofEvent = models.ForeignKey(EventType)
    reqServices = models.ManyToManyField(ServiceType)
    
    def __unicode__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=10)
    eventtypes = models.ManyToManyField(EventType)
    services = models.ManyToManyField(ServiceType)
    
    
    def __unicode__(self):
        return self.name