from django.http import (Http404, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

monthly_challenge = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "April",
    "may": "May",
    "june": "June",
    "july": "July",
    "august": "August",
    "september": "September",
    "octorber" : "Octorber",
    "november": "November",
    "december": None
}

def index(request):
    months = list(monthly_challenge.keys())
    return render(request,'challenges/index.html',{
        "months": months,
    })

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month,])
    return HttpResponseRedirect(redirect_path) 

def monthly_challenges(requset, month):
    try:
        challenges_text = monthly_challenge[month]
        return render(requset, 'challenges/challenge.html', {
            "text": challenges_text,
            "month_name": month,
        })
    except:
        raise Http404()
    