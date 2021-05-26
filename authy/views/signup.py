from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'
