from django.shortcuts import render, redirect
from first_app.forms import RegisterForm, changeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

def home(req) :
    return render(req, 'home.html')

def signup(req) :
    if not req.user.is_authenticated :
        if req.method == 'POST' :
            form = RegisterForm(req.POST)
            if form.is_valid() :
                form.save()
                messages.success(req, 'Account Created Successfully')
                print(form.cleaned_data)
        else :
            form = RegisterForm()
        return render(req, 'signup.html', {'form' : form})
    else :
        return redirect('profile')
    


def signin(req) :
    if not req.user.is_authenticated :
        if req.method == 'POST' :
            form = AuthenticationForm(request=req, data=req.POST)
            if form.is_valid() :
                name = form.cleaned_data['username']
                passwd = form.cleaned_data['password']
                user = authenticate(username=name, password=passwd)
                if user is not None :
                    login(req, user)
                    return redirect('profile')
        else :
            form = AuthenticationForm()

        return render(req, 'signin.html', {'form' : form})
    else :
        return redirect('profile')

    
def signout(req) :
    logout(req)
    return redirect('signin')


def profile(req) :
    if req.user.is_authenticated :
        if req.method == 'POST' :
            form = changeUserData(req.POST, instance=req.user)
            if form.is_valid() :
                form.save()
                messages.success(req, 'Account Updated Successfully')
                return redirect('profile')
        else :
            form = changeUserData(instance=req.user)
        return render(req, 'profile.html', {'form' : form, 'data' : req.user})
    else :
        return redirect('signup')
    

    
def pass_change(req) :
    if req.user.is_authenticated :
        if req.method == 'POST' :
            form = PasswordChangeForm(user=req.user, data=req.POST)
            if form.is_valid() :
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect('profile')
        else :
            form = PasswordChangeForm(user=req.user)
        return render(req, 'pass_change.html', {'form' : form})
    else :
        return redirect('signin')
    

def pass_change2(req) :
    if req.user.is_authenticated :
        if req.method == 'POST' :
            form = SetPasswordForm(user=req.user, data=req.POST)
            if form.is_valid() :
                form.save()
                update_session_auth_hash(req, form.user)
                return redirect('profile')
        else :
            form = SetPasswordForm(user=req.user)
        return render(req, 'pass_change.html', {'form' : form})
    else :
        return redirect('signin')
