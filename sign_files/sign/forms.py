"""
Application Forms.
"""

from django import forms
from django.utils.translation import ugettext as _


"""
WARNING --> The file size must be limited.
"""


class SignForm(forms.Form):
    """
    Form for signature view.
    """

    file = forms.FileField(label=_('File'), required=True)


class VerifyForm(forms.Form):
    """
    Verification view form.
    """

    file = forms.FileField(label=_('File'), required=True)
    sign = forms.CharField(
        label=_('Sign'), required=True, widget=forms.Textarea)
