import sesame.utils
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView

from .forms import EmailLoginForm


def profile(request):
    return render(request, "util/profile.html", locals())


class EmailLoginView(FormView):
    template_name = "util/email_login.html"
    form_class = EmailLoginForm

    def get_user(self, email):
        """Find the user with this email address."""
        User = get_user_model()
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(username=email, email=email)
            user.set_unusable_password()
            return user

    def create_link(self, user):
        """Create a login link for this user."""
        link = reverse("sesame-login-auth")
        link = self.request.build_absolute_uri(link)
        link += sesame.utils.get_query_string(user)
        return link

    def send_email(self, user, link):
        """Send an email with this login link to this user."""
        user.email_user(
            subject="Log in to HF",
            message=f"""\
Hello,

You requested that we send you a link to log in to our app:

    {link}

Thank you for using django-sesame!
""",
        )

    def email_submitted(self, email):
        user = self.get_user(email)
        if user is None:
            # Ignore the case when no user is registered with this address.
            # Possible improvement: send an email telling them to register.
            print("user not found:", email)
            return
        link = self.create_link(user)
        self.send_email(user, link)

    def form_valid(self, form):
        self.email_submitted(form.cleaned_data["email"])
        return render(self.request, "util/email_login_success.html")
