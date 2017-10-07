from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
from django.http import Http404

from . import forms
from .logic import DigitalSignature


class HomeView(TemplateView):
    """
    docstring for HomeView
    """

    template_name = "sign/home.html"


class SignView(View):
    """
    ....
    """

    template_name = "sign/sign.html"
    form_class = forms.SignForm

    def get(self, request):
        form = self.form_class

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        post = getattr(request, 'POST', None)
        files = getattr(request, 'FILES', None)
        form = self.form_class(post, files)
        context = {'form': form}

        if form.is_valid():
            sign = DigitalSignature.sign_file(form.files.get('file'))
            context.update({'sign': sign})

        return render(request, self.template_name, context)


class VerifyView(View):
    """
    ....
    """

    def get(self, request):
        raise Http404('Working ...')
