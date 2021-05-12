from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article

# Create your views here.
def welcome(request):
    return render (request,'welcome.html')


def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html',{"date":date,})




def past_days_news(request, past_date):

    try:
        # Converts date from the string 
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error whem Valueaerror is thrown
        raise Http404()
    if date == dt.date.today():
        return redirect(news_today)
    news=Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})

def news_today(request):
    date=dt.date.today()
    news=Article.todays_news()
    return render(request,'all-news/todays-news.html', {"date":date,"news":news})

