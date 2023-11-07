from Crypto.PublicKey import RSA
from Crypto.Cipher import ARC4
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
import base64

class Crypto:

    @staticmethod
    def get_private_key(file_path, password=None):
        private_key = RSA.import_key(
            open(file_path, 'r').read(), passphrase=password)
        return private_key

    @staticmethod
    def get_rsa_key(file_path):
        # Importing keys from files, converting it into the RsaKey object
        public_key = RSA.import_key(open(file_path, 'r').read())
        return public_key

    @staticmethod
    def encrypt(src_data, public_key):
        random_key = get_random_bytes(16)

        cipher = PKCS1_v1_5.new(public_key)
        enc_key = cipher.encrypt(random_key)
        cipher = ARC4.new(random_key)
        enc_data = cipher.encrypt(src_data)
        enc_data = base64.b64encode(enc_data).decode('utf-8')
        enc_key = base64.b64encode(enc_key).decode('utf-8')

        return enc_data, enc_key

    @staticmethod
    def decrypt(enc_data, private_key, enc_key):
        enc_data = base64.b64decode(enc_data.encode('utf-8'))
        enc_key = base64.b64decode(enc_key.encode('utf-8'))

        decrypt = PKCS1_v1_5.new(private_key)
        decrypted_key = decrypt.decrypt(enc_key, get_random_bytes(16))
        cipher = ARC4.new(decrypted_key)
        xml_data = cipher.decrypt(enc_data)

        return xml_data

