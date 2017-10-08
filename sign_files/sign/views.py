"""
Views of the application.
"""

from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render

from . import forms
from .logic import DigitalSignature


class HomeView(TemplateView):
    """
    Class for home view.
    Render a simple template.
    """

    template_name = "sign/home.html"


class SignView(View):
    """
    Class for the view that signs a file.
    Support two methods (GET and POST).
    """

    template_name = "sign/sign.html"
    form_class = forms.SignForm

    def get(self, request):
        # Get method.
        form = self.form_class

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # POST method.

        # Data.
        post = getattr(request, 'POST', None)
        files = getattr(request, 'FILES', None)
        form = self.form_class(post, files)
        context = {'form': form}

        if form.is_valid():
            # Sign
            sign = DigitalSignature.sign_file(form.files.get('file'))
            context.update({'sign': sign})

        return render(request, self.template_name, context)


class VerifyView(View):
    """
    Class for the view that checks a file.
    Support two methods (GET and POST).
    """

    template_name = "sign/verify.html"
    form_class = forms.VerifyForm

    def get(self, request):
        # Get method.
        form = self.form_class

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # POST method.

        # Data.
        post = getattr(request, 'POST', None)
        files = getattr(request, 'FILES', None)
        form = self.form_class(post, files)
        context = {'form': form}

        if form.is_valid():
            data = {'file': form.files.get('file'),
                    'sign': form.data.get('sign')
                    }

            # Improve with Messages (Framework).
            # Verify and return message.
            if DigitalSignature.verify_file(data):
                context.update({'msg': 'OK'})
            else:
                context.update({'msg': 'Error'})

        return render(request, self.template_name, context)
