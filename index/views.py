from django.shortcuts import render

# Create your views here.
from schedule.models import DaySchedule


def index(request):
    return render(request, 'index.html', {"data":DaySchedule.objects.all().order_by('week')})