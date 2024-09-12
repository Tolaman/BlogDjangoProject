from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
  
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # Create a new form with the data that was within the 'request.POST'
        if form.is_valid(): # Does the backend check with the 'UserCreationForm'
            form.save() # saving the user
            username = form.cleaned_data.get('username') # take the value of the username
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # if if the form isn't valid, the page's gonna return the form with the insered values
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
