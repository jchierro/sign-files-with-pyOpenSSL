from django.utils.translation import ugettext as _
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from sign import forms

BASE_DIR = getattr(settings, 'BASE_DIR', None)
SIGN = b'ElOiYAhn3fWNSQMAr/IYNkRweh+Q6FGLPUNw1tTRpfMzE+01OJ63Til0d0mRkZ2i0UahgO5KaTRu+bGZOOXrs2iOThZcbpFVp31AGdoSainrEjfapQphtXxaAqDq/2CUcIVkMwORT1jlXpZGUUJuOEgR1c4Z8yyjBUZeF8KGSmrCWmxlh4r6Z3UeIrlVGGW0fuZjRvYpJusPWzbQZZ//j886AT2XLKUrllAvEX/ATo9wzjfQ5ukdKJHQD+Eab3RR31FVLuI46ofseYGLtRrr7s/lC9kYpEw3q5PjBPqxEg2Sgdjfa2r8DZ8HiWHyHhqKedwpMtxYjW4MAuk7aiWIpQ=='


class ViewsTestCase(TestCase):

    def test_0_sign(self):
        # GET Method --> Success
        response = self.client.get(reverse('sign'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('form'), forms.SignForm)

        # POST Method --> Success
        path = BASE_DIR + '/sign/tests/file_for_tests.txt'
        file = open(path, 'rb')

        response = self.client.post(reverse('sign'), {'file': file})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('sign'), SIGN)

        # POST Method --> Error
        response = self.client.post(reverse('sign'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

    def test_1_verify(self):
        # GET Method --> Success
        response = self.client.get(reverse('verify'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get('form'), forms.VerifyForm)

        # POST Method --> Sucess
        path = BASE_DIR + '/sign/tests/file_for_tests.txt'
        file = open(path, 'rb')

        response = self.client.post(reverse('verify'), {'file': file,
                                                        'sign': str(SIGN, 'utf-8')})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _(
            'The file has been successfully checked.'))

        # POST Method --> Error
        response = self.client.post(reverse('verify'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context.get('form').errors)

        response = self.client.post(reverse('verify'), {'file': file,
                                                        'sign': 'abc'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _(
            'The signature does not have a valid format.'))

        path = BASE_DIR + '/sign/tests/file_for_tests_2.txt'
        file = open(path, 'rb')
        response = self.client.post(reverse('verify'), {'file': file,
                                                        'sign': str(SIGN, 'utf-8')})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _(
            'The file cannot be verified with that signature.'))

    def test_2_home(self):
        # GET Method --> Success
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
