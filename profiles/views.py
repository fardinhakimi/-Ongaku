# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from .forms import UserForm
from .forms import LoginForm
from .forms import ProfileForm
from django.shortcuts import  render, redirect
# helps in authentication and login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# user registarion form
class UserRegistration(View):

    # display form
    template_name = "profiles/registration_form.html"
    form_class = UserForm

    def get(self, request):
        user_form = self.form_class(None)  # no context
        profile_form = ProfileForm
        return render(request, self.template_name, {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self,request):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # get data for authentication
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            # authenticate the user
            user = authenticate(username=username, password=password)

            if user is not None:
              login(request, user)
            return redirect("music:index")

        else:
            user_form = UserForm(prefix="user")
            profile_form = ProfileForm(prefix="profile")
        context = {
            "user_form": user_form,
            "profile_form": profile_form
        }

        return render(request, self.template_name, context)


class Dashboard(View):

    def get(self, request):
        #profile = request.user.profile
        #profile_form = ProfileForm(instance=profile)
        return render(request,"profiles/dashboard.html",
    )


class UpdateAccount(View):

    def get(self, request):
        account_form = UserForm(request.POST, instance=request.user)
        return render(request, "profiles/dashboard.html",context={"user_form": account_form,
         })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)

        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
         profile_form.save()
        return redirect("music:index")


class ChangePassword(View):

    def post(self, request):
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profiles:dashboard',{"active_tab": "settings"})
            else:
                messages.error(request, 'Please correct the error below.')

    def get(self, request):
        change_password_form = PasswordChangeForm(request.user)
        return render(request, 'profiles/dashboard.html', {
            'change_password_form': change_password_form
})



# login the user
class LoginView(View):
    # show when method is get
    template_name = "profiles/login.html"
    form_class = LoginForm

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{"form":form})
    # show when method is post

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            formData = form.cleaned_data
            username = formData.get("username")
            password = formData.get("password")
            # attempt for user authentication
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # get current user
                current_user = request.user
                # set session variabes

                return redirect("music:index")
        # render the login from again
        messages.error(request, 'Invalid login credentials')
        return render(request, self.template_name, {"form": form})

# logout the user
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("music:index")


