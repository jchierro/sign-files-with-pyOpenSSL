"""
Logical layer of the application.
"""

import base64
import logging

from OpenSSL import crypto
from django.conf import settings

# Settings Variables
CERTIFICATE_PATH = getattr(settings, 'CERTIFICATE_PATH', None)
PASSWORD = getattr(settings, 'PASSWORD', None)
DIGEST = getattr(settings, 'DIGEST', None)

log = logging.getLogger(__name__)


class DigitalSignature(object):
    """
    Class with two static methods that sign or validate a file.
    """

    @staticmethod
    def sign_file(data):
        # Create object.
        certificate = Certificate(CERTIFICATE_PATH, PASSWORD)

        # Call crypto.sign --> (Private key, data, digest).
        sign = crypto.sign(certificate.private_key, data.read(), DIGEST)
        data.close()

        # Binaty to base64.
        return base64.b64encode(sign)

    @staticmethod
    def verify_file(data):
        # Create object.
        certificate = Certificate(CERTIFICATE_PATH, PASSWORD)

        # Data.
        file = data.get('file')
        # Str to base64 to binary.
        sign = base64.decodebytes(str.encode(data.get('sign')))
        result = False

        try:
            # Call crypto.verify --> (Object x509, sign, data, digest).
            crypto.verify(certificate.x509, sign, file.read(), DIGEST)
            result = True
        except crypto.Error as error:
            # Log.
            log.error(
                '[pyOpenSSL - Verify]: {error} '.format(error=str(error)))
        finally:
            file.close()

        return result


class Certificate(object):
    """
    Class responsible for processing the FNMT certificate.
    """

    def __init__(self, certificate_path, password):
        super(Certificate, self).__init__()
        self.__certificate_path = certificate_path
        self.__password = password

        self.__read_certificate()

        self.pkcs12 = self.__load_pkcs12()
        self.x509 = self.__get_x509()
        self.private_key = self.__get_private_key()

    def __read_certificate(self):
        # Read certificate.
        try:
            file = open(self.__certificate_path, "rb")
            self.__certificate_buffer = file.read()
            file.close()
        except IOError as error:
            # Log.
            log.error('[Class Certificate]: {error} '.format(error=str(error)))
            raise error

    def __load_pkcs12(self):
        # Load pkcs12.
        return crypto.load_pkcs12(self.__certificate_buffer, self.__password)

    def __get_x509(self):
        # Get x509.
        return self.pkcs12.get_certificate()

    def __get_private_key(self):
        # Get the private key.
        return self.pkcs12.get_privatekey()
