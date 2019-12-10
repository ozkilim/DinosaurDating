from datetime import date

import urllib3
from django.core.mail import send_mail
from django.http import response
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
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
            obj.event_id = event
            obj.save()
            men_number = Atendee.objects.filter(gender='male', event_id=id)
            woman_number = Atendee.objects.filter(gender='female', event_id=id)
            if obj.gender == 'male':
                if len(men_number) >= 10:
                    return render(request, "sorry.html")
                return redirect(reverse('mainsite:pay', kwargs={ 'charge': event_price }))
            else:
                if len(woman_number) >= 10:
                    return render(request, "sorry.html")
                return redirect(reverse('mainsite:pay', kwargs={ 'charge': event_price }))

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
        context['charge']=self.kwargs['charge']
        return context

def charge(request):
    if request.method == 'POST':
        amount = request.POST.get('chargepass')
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )

        # here is where we also send if email..
        # make sure it only sends if payment goes through.... may need to pass through perameters to the f'n..
        mail_subject = 'See you soon!'
        message = 'we look forward to seeing you soon!'
        user_email = request.POST.get('stripeEmail')
        print(user_email)
        send_mail(
            mail_subject,
            message,
            'fridgeflipapp@gmail.com',
            [user_email],
            fail_silently=False,
        )


        return render(request, 'charge.html')




