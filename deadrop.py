import os
import socket
import struct
import sys
import threading

from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding,PublicFormat

def generate_keypair():
    priv = X25519PrivateKey.generate()
    pub_key = priv.public_key()
    pub_bytes = pub_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
    return priv, pub_bytes

def derive_key(private_key, peer_pub_bytes):
    pass

def encrypt(key, plaintext):
    pass

def decrypt(key, data):
    pass
