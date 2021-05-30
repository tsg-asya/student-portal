from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin


class SignUpView(UserPassesTestMixin, TemplateView):
    template_name = 'registration/signup.html'

    def test_func(self):
        return not self.request.user.is_authenticated

    # def dispatch(self, request, *args, **kwargs):
    #     user = request.user
    #     if user.is_authenticated:
    #         return redirect('index')
    #     return super().dispatch(request, *args, **kwargs)
