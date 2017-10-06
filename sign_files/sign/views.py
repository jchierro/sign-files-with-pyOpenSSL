from django.views.generic import TemplateView

from django.http import Http404


class HomeView(TemplateView):
    """
    docstring for HomeView
    """

    template_name = "sign/home.html"


def sign(request):
    """
    ...
    """

    raise Http404('Working ...')


def verify(request):
    """
    ...
    """

    raise Http404('Working ...')
