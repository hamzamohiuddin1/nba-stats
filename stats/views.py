from django import forms
from django.shortcuts import render

import markdown2
import random
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.

def homepage(request):
    return render(request, 'stats/homepage.html')


def player(request, name):
    return render(request, "stats/player.html", {
        'name': name
    })


def search(request):
    query = request.GET['q'].lower()
    return player(request, query)
