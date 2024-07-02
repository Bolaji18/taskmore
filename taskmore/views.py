from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import info
from django.http import JsonResponse

def home(request):
    return render(request=request, template_name="index.html", context={})
def getprofile(request):
    infos= info.objects.all()
    return JsonResponse({"infos":list(infos.values())})
def load_data(request):
    infos = info.objects.filter(status="In Progress")
    return render(request, 'loaddata.html', {'infos': infos})
def completed(request):
    infos = info.objects.filter(status="Completed")
    return render(request, 'loaddata.html', {'infos': infos})
def Overdue(request):
    infos = info.objects.filter(status="Overdue")
    return render(request, 'loaddata.html', {'infos': infos})