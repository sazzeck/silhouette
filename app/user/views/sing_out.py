from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy


class SingOutUserView(LogoutView):

    def get_success_url(self):
        return reverse_lazy("main")
