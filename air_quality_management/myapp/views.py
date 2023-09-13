from django.shortcuts import render, get_object_or_404, redirect
from .models import AirQualityData, Location, Pollutant, Sensor
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from django.views import View
from .forms import LoginForm, RegisterForm


def homepage(request):
    """
    View for the homepage.
    """
    # You can add logic here to fetch data from your models if needed
    # For now, we'll render the homepage template with some dummy data
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'homepage.html', context)


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Welcome back!')
                return HttpResponseRedirect('user')

        messages.error(request, f'Invalid username or password')
        return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, f"You've been logged out.")
    return HttpResponseRedirect('login')


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully')
            login(request, user)
            return HttpResponseRedirect('user')
        else:
            return render(request, 'registration/register.html', {'form': form})


def user_view(request):
    """
    View to display a list of air quality data.
    """
    dummy_data = []

    context = {
        'data': dummy_data,
    }
    return render(request, 'user/user_profile.html', context)


class city_details(View):
    template_name = 'city_details.html'

    def get(self, request, *args, **kwargs):
        # You can fetch data for the city here if needed
        city_data = {}

        context = {
            'city_data': city_data,
        }

        return render(request, self.template_name, context)


def air_quality_data_list(request):
    """
    View to display a list of air quality data.
    """
    air_quality_data = AirQualityData.objects.all()
    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'data/air_quality_data_list.html', context)


def air_quality_data_detail(request, data_id):
    """
    View to display details of a specific air quality data point.
    """
    air_quality_data = get_object_or_404(AirQualityData, data_id=data_id)
    context = {
        'air_quality_data': air_quality_data,
    }
    return render(request, 'my_app/air_quality_data_detail.html', context)

@login_required
def profile(request):
    return render(request, 'user/user_profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, _('Your profile is updated successfully'))
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'user/profile_edit.html', {'user_form': user_form})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_message = _('Successfully Changed Your Password')
    success_url = reverse_lazy('users-profile')
