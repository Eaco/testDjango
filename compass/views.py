from django.shortcuts import render, redirect
from django.http import*
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
	return render(request, 'compass/signin.html', {})

def login_request(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        print("found user")
        login(request, user)
        return HttpResponseRedirect('/main')
        # Redirect to a success page.
    else:
        print("user not found")
        return null
        # Return an 'invalid login' error message.

@login_required()
def main_view(request):
	print("user authenticated successfully")
	print(request.user)
	return render(request, 'compass/test.html', {})