import struct
import sys
from os import urandom as randbytes
from base64 import b64decode

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import algorithms, modes
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.hashes import SHA1, Hash


backend = default_backend()


class UniverseKey:

    Public = backend.load_der_public_key(b64decode("""
MIGdMA0GCSqGSIb3DQEBAQUAA4GLADCBhwKBgQDf7BrWLBBmLBc1OhSwfFkRf53T
2Ct64+AVzRkeRuh7h3SiGEYxqQMUeYKO6UWiSRKpI2hzic9pobFhRr3Bvr/WARvY
gdTckPv+T1JzZsuVcNfFjrocejN1oWI0Rrtgt4Bo+hOneoo3S57G9F1fOpn5nsQ6
6WOiu4gZKODnFMBCiQIBEQ==
"""))


def generate_session_key(challenge=b''):
    session_key = randbytes(32)
    encrypted_key = UniverseKey.Public.encrypt(session_key + challenge,
                                               OAEP(MGF1(SHA1()), SHA1(), None))
    return session_key, encrypted_key


def symmetric_encrypt(data, key, hmac_key=None):
    if hmac_key:
        prefix = randbytes(3)
        hmac = HMAC(hmac_key, SHA1(), backend)
        hmac.update(prefix + data)
        iv = hmac.finalize()[:13] + prefix
    else:
        iv = randbytes(16)

    return symmetric_encrypt_with_iv(data, key, iv)


def symmetric_encrypt_with_iv(data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend)
    encryptor = cipher.encryptor()
    enc_iv = encryptor.update(iv) + encryptor.finalize()

    padder = PKCS7(128).padder()
    pad_data = padder.update(data) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend).encryptor()
    enc_data = encryptor.update(pad_data) + encryptor.finalize()

    return enc_iv + enc_data


def symmetric_decrypt(data, key, hmac_key=None):
    enc_iv, enc_data = data[:16], data[16:]
    decryptor = Cipher(algorithms.AES(key), modes.ECB(), backend).decryptor()
    iv = decryptor.update(enc_iv) + decryptor.finalize()

    decryptor = Cipher(algorithms.AES(key), modes.CBC(iv), backend).decryptor()
    unenc_data = decryptor.update(enc_data) + decryptor.finalize()

    unpadder = PKCS7(128).unpadder()
    unenc_data = unpadder.update(unenc_data) + unpadder.finalize()

    if hmac_key:
        prefix = iv[13:]
        hmac = HMAC(hmac_key, SHA1(), backend)
        hmac.update(prefix + unenc_data)
        hmac_msg = hmac.finalize()
        if hmac_msg[:13] != iv[:13]:
            raise RuntimeError("Unable to decrypt message, HMAC doesn't match. %s:%s" % (hmac_msg, iv))

    return unenc_data


def sha1_hash(data):
    sha = Hash(SHA1(), backend)
    sha.update(data)
    return sha.finalize()



