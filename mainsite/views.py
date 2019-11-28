from datetime import date

import urllib3
from django.http import response
from django.http import request
from django.shortcuts import render, redirect
from urllib3.util import url

from mainsite.forms import AtendeeForm
from mainsite.models import Events, Atendee
from speeddatingpainting import settings
from django.views.generic.base import TemplateView
import stripe
from django.shortcuts import render
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def landing(response):
    return render(response, "landing.html")


def events(response):
    events =[]
    for event in Events.objects.all():
        name = event.name
        date = event.date
        location = event.location
        image = event.image
        description = event.description
        id = event.id
        one_event = {"name":name,"date":date,"location":location,"image":image,"decription":description,'id':id}
        events.append(one_event)

    return render(response, "events.html",{"events":events})


def reserve(response):
    return render(response, "reserve.html")


def references(response):
    return render(response, "references.html")

def tickets(request,id):
    if request.method == 'POST':
        form = AtendeeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.signup_date = date.today()
            event = Events.objects.get(id=id).id
            event_price = Events.objects.get(id=id).price
            # later pass this through to payment..
            obj.event_id = event
            obj.save()
            men_number = Atendee.objects.filter(gender='male', event_id=id)
            woman_number = Atendee.objects.filter(gender='female', event_id=id)
            if obj.gender == 'male':
                if len(men_number) >= 10:
                    return render(request, "sorry.html", )
                return redirect('/pay')
            else:
                if len(woman_number) >= 10:
                    return render(request, "sorry.html", )
                return redirect('/pay')

    form = AtendeeForm()
    event = Events.objects.get(id=id)
    event_name = event.name
    event_date = event.date
    event_location = event.location
    event_price = event.price

    return render(request, "tickets.html", {"event_name":event_name, "event_date":event_date,'event_location':event_location, 'event_price':event_price, 'form':form },)


class pay(TemplateView):
    template_name = 'pay.html'
    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')




