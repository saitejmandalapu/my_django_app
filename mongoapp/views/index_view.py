from mongoapp.models import Details, LoginTime
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date
from datetime import timedelta
import logging


def index(request):
    data = {}
    return render(request, "mongoapp/index.html", data)


def create(request):
    choice1 = LoginTime(start_date=datetime.datetime.now() - timedelta(1), end_date=datetime.datetime.now())
    choice2 = LoginTime(start_date=datetime.datetime.now() - timedelta(2), end_date=datetime.datetime.now())
    choice3 = LoginTime(start_date=datetime.datetime.now() - timedelta(3), end_date=datetime.datetime.now())
    choice4 = LoginTime(start_date=datetime.datetime.now() - timedelta(4), end_date=datetime.datetime.now())

    activity_periods = [choice1, choice2, choice3, choice4]

    poll = Details(real_name="Egon Spengler", tz='Asia/Kolkata', activity_periods=activity_periods)
    poll.save()
    return HttpResponseRedirect(reverse("mongoapp:show"))


def show(request):
    data = {}
    p = Details.objects.all()
    print(request)
    return render(request, "mongoapp/show.html", data)


def delete(request, document_id):
    Details.objects.filter(id=document_id).delete()
    return HttpResponseRedirect(reverse("mongoapp:show"))
