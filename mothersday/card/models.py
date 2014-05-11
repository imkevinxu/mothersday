from django.db import models

# Create your models here.
class Card(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    phone = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    image = models.TextField(blank=True)
    a1 = models.TextField(blank=True)
    a2 = models.TextField(blank=True)
    a3 = models.TextField(blank=True)
    a4 = models.TextField(blank=True)
    a5 = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.phone, self.name)

    def first_name(self):
        if self.name:
            return self.name.split(" ")[0]
        return None
