from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import info
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from .forms import createform
from datetime import datetime

def home(request):
    if request.method == "POST":
        selected = request.POST.get("query")
        values = info.objects.filter(description__icontains=selected).values()
        return render(request=request, template_name="loaddata.html", context={'infos': values})

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
         return redirect('home')



def user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)


                welcome = f" {username}."
                return redirect('home')


            else:
                 form = "Invalid Username or Password"
                 return render(request=request, template_name="form.html", context={"register_form":form})

        else:
             form = "Invalid Username or Password"
             return render(request=request, template_name="form.html", context={"register_form":form})
    form = AuthenticationForm()
    create = "new/"
    used = "Create New User"
    life = "Login"
    ball="Login"
    return render(request, "form.html", {"register_form":form,  'new':create, 'used':used, 'life':life, 'all':ball})

def new(request):
   if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           return redirect('/login/')

   form= NewUserForm()
   life= "Create"
   used = "Already have account Login here "
   ball="Create New User"

   return render(request=request, template_name="form.html", context={"register_form":form, 'life':life, 'login':used, 'all':ball})


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        status = request.POST.get("status")
        priority = request.POST.get("priority")
        due_date = datetime.now()
        category = request.POST.get("category")
        assigned_to = request.user
        my_worker = info(title=title,assigned_to=assigned_to, category=category,due_date=due_date, priority=priority, description=description, status=status)
        my_worker.save()
        return redirect('home')
    form = createform()
    life="Submit"
    return render(request=request,  template_name="form.html", context={"register_form":form, "life":life})
