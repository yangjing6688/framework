import base64
from Crypto.Cipher import DES3


def des3_encrypt(msg):
    """Returns the encryption of *msg*, converted to Base64."""
    key = b'99a3d014b62293332b85c3ab'
    des3 = DES3.new(key, DES3.MODE_CBC, b'\0\0\0\0\0\0\0\0')
    e_msg = base64.b64encode(des3.encrypt(pkcs5_pad(msg).encode("utf-8")))
    if not isinstance(e_msg, str):
        e_msg = e_msg.decode('utf-8')
    return e_msg


def des3_decrypt(msg):
    """Returns the decrypted *msg* after converting from Base64."""
    key = b'99a3d014b62293332b85c3ab'
    des3 = DES3.new(key, DES3.MODE_CBC, b'\0\0\0\0\0\0\0\0')
    return pkcs5_unpad(des3.decrypt(base64.b64decode(msg).encode("utf-8")))


def pkcs5_pad(msg):
    """Pads the *msg* using PKCS #5 padding."""
    block_size = 8
    pad_length = block_size - len(msg) % block_size
    pad_char = chr(block_size - len(msg) % block_size)
    return msg + pad_length * pad_char


def pkcs5_unpad(msg):
    """Unpads the *msg* according to PKCS #5."""
    if isinstance(msg, str):
        return msg[0:-ord(msg[-1])]
    else:  # Python 3
        return msg[0:-msg[-1]].decode('utf-8')
