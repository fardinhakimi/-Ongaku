
from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from . import views
app_name = "profiles"
urlpatterns = [
url(r'^register/$', views.UserRegistration.as_view(), name="register"),
url(r'^dashboard/$',login_required(views.Dashboard.as_view()), name="dashboard"),
url(r'^dashboard/change-password/$',login_required(views.ChangePassword.as_view()), name="change-password"),
url(r'^login/$', views.LoginView.as_view(), name="login"),
url(r'^logout/$', login_required(views.LogoutView.as_view()), name="logout"),
]
