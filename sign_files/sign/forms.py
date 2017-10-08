"""
Application Forms.
"""

from django import forms
from django.utils.translation import ugettext as _

from .logic import to_binary


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
        label=_('Signature'), required=True, widget=forms.Textarea)

    def clean(self):
        cleaned_data = super(VerifyForm, self).clean()
        sign = cleaned_data.get('sign')

        if sign:
            binary_sign = to_binary(sign)
            if not binary_sign:
                self.add_error(
                    'sign', _('The signature does not have a valid format.'))
            else:
                cleaned_data.update({'sign': binary_sign})

        return cleaned_data
