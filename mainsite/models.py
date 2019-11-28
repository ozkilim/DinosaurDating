from django.db import models

# Create your models here.
class Events(models.Model):
	name=models.CharField(max_length=100)
	date=models.DateTimeField(max_length=100)
	location=models.CharField(max_length=100)
	image=models.ImageField()
	description=models.CharField(max_length=100)
	price = models.IntegerField(null=True)


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

