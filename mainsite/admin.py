from django.contrib import admin

# Register your models here.
from django.contrib import admin
from mainsite.models import Events,Atendee

admin.site.register(Events)

admin.site.register(Atendee)

