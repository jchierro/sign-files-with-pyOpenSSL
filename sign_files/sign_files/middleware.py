"""
Middlewares
"""

from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.conf import settings

# 10 MB
MAX_UPLOAD_SIZE = getattr(settings, 'MAX_UPLOAD_SIZE', 10485760)


class RequestSizeMiddleware(object):
    """
    Middleware to control the size of requests.
    """

    def __init__(self, get_response):
        """
        One-time configuration and initialization.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Controls the size of the request.
        """
        response = self.get_response(request)
        content = request.META.get('CONTENT_LENGTH')

        if content and int(content) > MAX_UPLOAD_SIZE:
            message = '<h1>{0}</h1>'.format(
                _('Has exceeded the size of the request.'))
            return HttpResponse(message)

        return response
