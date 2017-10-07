from django import forms
from django.utils.translation import ugettext as _


class SignForm(forms.Form):
    """
    ....
    """

    file = forms.FileField(label=_('File'), required=True)
