from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from nodes.models import Division

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST["password1"])
        user.save()
        user.userprofile.monthly_budget = request.POST['budget']
        user.userprofile.energy_plan = request.POST['energy_plan']
        user.save()
        user.userprofile.save()
        login(request, user)
        return redirect('create_division')
    else:
        # return HttpResponse('Get method not allowed')
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def create_division(request):
    print(request.method)
    if request.method =='POST':
        division = Division(name = request.POST['name'])
        division.save()
        user = request.user
        user.userprofile.divisions.add(division)
        user.save()
    else:
        return render(request, 'users/create_division.html')