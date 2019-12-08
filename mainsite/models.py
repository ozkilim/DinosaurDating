from unittest.test.test_case import Test

from django.db import models

# Create your models here.
class Events(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateTimeField(max_length=100)
	location=models.CharField(max_length=100)
	image=models.ImageField()
	description=models.CharField(max_length=100)
	price = models.IntegerField(null=True)

	def __str__(self):
		return self.name

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'name':
			return Atendee(queryset=Test.objects.all())
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


class Atendee(models.Model):
	MY_CHOICES = (
		('male','male'),
		('female','female'),
		('other','other'),
	)
	user_name=models.CharField(max_length=100)
	signup_date=models.DateTimeField(max_length=100)
	email=models.CharField(max_length=100)
	looking_for=models.CharField(max_length=100)
	age = models.IntegerField(null=True)
	gender = models.CharField(null=True, max_length=20, choices=MY_CHOICES)
	event = models.ForeignKey(Events, on_delete=models.CASCADE, null=True)
	phone_number = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.user_name

