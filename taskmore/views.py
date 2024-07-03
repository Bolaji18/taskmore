from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import info
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

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

@require_POST
def delete(request):
     id = request.POST.get('task_id')
     try:
         task = get_object_or_404(info, id=id)
         task.delete()
         return JsonResponse({'message': 'Item deleted successfully'})
     except Exception as e:
         return JsonResponse({'error': str(e)}, status=500)

def deleted (request, id):
         task = get_object_or_404(info, id=id)
         task.delete()
         return render(request, 'index.html', {})
