"""
.....

"""

import base64

from OpenSSL import crypto
from django.conf import settings


PEM_PATH = getattr(settings, 'PEM_PATH', None)
PASSWORD = getattr(settings, 'PASSWORD', None)
DIGEST = getattr(settings, 'DIGEST', None)


class DigitalSignature(object):
    """
    docstring for DigitalSignature
    """

    @staticmethod
    def sign_file(data):
        certificate = Certificate(PEM_PATH, PASSWORD)
        private_key = certificate.get_private_key()

        sign = crypto.sign(private_key, data.read(), DIGEST)
        data.close()

        return base64.b64encode(sign)

    @staticmethod
    def verify_file(data):
        pass


class Certificate(object):
    """
    docstring for Certificate
    """

    def __init__(self, pem_path, password):
        super(Certificate, self).__init__()
        self.pem_path = pem_path
        self.password = password
        self.crypto = crypto.FILETYPE_PEM
        self.pem = None

        self.__read_certificate()

    def __read_certificate(self):
        try:
            file = open(self.pem_path, "rb")
            self.pem = file.read()
            file.close()
        except IOError as error:
            raise error

    def get_private_key(self):
        """
        Improve

        if self.pem.startswith('-----BEGIN '):
            return crypto.load_privatekey(self.crypto, self.pem, self.password)
        else:
        """
        return crypto.load_pkcs12(self.pem, self.password).get_privatekey()
