from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from user.forms import SingInForm


class SingInUserView(LoginView):
    form_class = SingInForm
    template_name = "user/sing_in.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        data = {
            "title": "sing in"
        }
        context.update(data)
        return context

    def get_success_url(self):
        return reverse_lazy("main")
