from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import context

# Create your views here


from todos.forms import *
from todos.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from todos.models import Task
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    context = RequestContext(request)
    task_list = Task.objects.all()
    context_dict = {'tasks': task_list}
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.create_task(
            title=form.cleaned_data['title'],
            ownerid={{ user.username }},
            description=form.cleaned_data['description']
            )
            return HttpResponseRedirect('/home/')
    
    return render_to_response(
        'home.html', context_dict, context, {'form': form}
        )
    
