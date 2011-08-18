from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_dj
from django.contrib.auth import login as login_dj
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django import forms


@login_required
def index(request):
    user = request.user
    context = {'username': user.username,
            'email': user.email,
            }

    return render_to_response('profile.tpl', context)

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    redirect_to = forms.CharField(widget=forms.HiddenInput())

def login(request):
    redirect_to = '/'
    if request.user.is_authenticated():
        return redirect(index)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            redirect_to = form.cleaned_data['redirect_to']
            user = authenticate(username=form.cleaned_data['login'],
                    password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login_dj(request, user)
                    return redirect(redirect_to)
                else:
                    context = {'form': form,
                            'next': redirect_to,
                            'error': 'Your account is disabled.'}
                    context.update(csrf(request))
                    return render_to_response('users/login_form.tpl', context)
            else:
                context = {'form': form,
                        'next': redirect_to,
                        'error': 'Your login or password is invalid.'}
                context.update(csrf(request))
                return render_to_response('users/login_form.tpl', context)
        else:
            context = {'error': 'You submitted an invalid form.',
                    'form': form}
            context.update(csrf(request))
            return render_to_response('users/login_form.tpl', context)
    else:
        if request.GET.get('next') is not None:
            redirect_to = request.GET.get('next')
        form = LoginForm(initial={'redirect_to': redirect_to})
        context = {'form': form, 'next': redirect_to}
        context.update(csrf(request))
        return render_to_response('users/login_form.tpl', context)

# @login_required would be stupid here, because it would ask to login in
# order to logout.
def logout(request):
    if request.user.is_authenticated():
        logout_dj(request)
    return redirect('/')

class RegistrationForm(forms.Form):
    login = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    redirect_to = forms.CharField(widget=forms.HiddenInput())

def register(request):
    if request.user.is_authenticated():
        return redirect(index)
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                context = {'form': form,
                        'error': 'The passwords do not match.'}
                context.update(csrf(request))
                return render_to_response('users/register_form.tpl', context)
            elif User.objects.filter(username=form.cleaned_data['login']).exists():
                context = {'form': form,
                        'error': 'This username already exists.'}
                context.update(csrf(request))
                return render_to_response('users/register_form.tpl', context)
            else:
                user = User.objects.create_user(form.cleaned_data['login'],
                        email=form.cleaned_data['email'],
                        password=form.cleaned_data['password'])
                user.save()
                return redirect(form.cleaned_data['redirect_to'])
        else:
            context = {'error': 'You submitted an invalid form.',
                    'form': form,
                    'next': request.GET.get('next')}
            context.update(csrf(request))
            return render_to_response('users/register_form.tpl', context)
        user = authenticate(username=form.cleaned_data['login'],
                password=form.cleaned_data['password'])
        assert user is not None
        assert user.is_active
    else:
        form = RegistrationForm(initial={'redirect_to': request.GET.get('next')})
        context = {'form': form, 'next': request.GET.get('next')}
        context.update(csrf(request))
        return render_to_response('users/register_form.tpl', context)
