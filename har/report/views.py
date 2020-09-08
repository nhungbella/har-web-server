from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import CreateUserForm, ReportForm
from .models import Report


def render_connection_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        # check user exist in database
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('reports/')
        # add value in form
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # login after create user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('reports/')
        else:
            messages.error(request,'Username or Password is incorrect!')
        
    context = {'form': form}
    template_name = 'connection.html'
    return render(request, template_name, context)


@login_required(login_url='login')
def render_report_creation_view(request):
    # check if login successfull
    if request.user.is_authenticated:
        user = request.user
    # create form
    form = ReportForm()
    if request.method == 'POST':
        # add data in form
        form = ReportForm(request.POST)
        if form.is_valid():
            # create second object
            report = form.save(commit=False)
            report.user = user
            report.save()
            return redirect('reports')
        else:
            messages.error(request, "Error")

    context = {'form': form}
    template_name = 'report_creation.html'
    return render(request, template_name, context)

@login_required(login_url='login')        
def render_report_update_view(request, number_report):
    form = ReportForm()
    # get report follow user login created    
    report = Report.objects.filter(id=number_report)
    if len(report) == 0 or request.user != report[0].user:
        return redirect('report')
    # put data in form
    form = ReportForm(instance=report[0])
    if request.method == 'POST':
        form = ReportForm(
            request.POST, 
            instance=report[0]
        )
        if form.is_valid():
            form.save()
            return redirect('reports')

    context = {'form': form}
    template_name = 'report_update.html'
    return render(request, template_name, context)

@login_required(login_url='login')  
def render_reports_view(request):
    report = Report.objects.filter(user=request.user).order_by('creation_time')
    
    if request.method == "POST":
        return redirect('report')

    context = {'form': report}
    template_name = 'reports.html'
    return render(request, template_name, context)

@login_required(login_url='login')  
def render_report_deletion_view(request, number_report):
    report = Report.objects.get(pk=number_report)
    report.delete()
    return redirect('reports')

def logoutUser(request):
    logout(request)
    return redirect('login')