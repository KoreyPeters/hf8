"""
URL configuration for hf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from sesame.views import LoginView

import util
from util.views import EmailLoginView

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("profile/", util.views.profile, name="profile"),
    path("login/", EmailLoginView.as_view(), name="sesame-login"),
    path("login/auth/", LoginView.as_view(), name="sesame-login-auth"),
    path("polium/", include("polium.urls"), name="polium")
]
