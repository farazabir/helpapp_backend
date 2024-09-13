from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Parent(models.Model):
    section = models.ForeignKey(
        Section, related_name='parents', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey(
        Parent, related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=15, blank=True, null=True)
    location = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
