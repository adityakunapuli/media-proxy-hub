"""
This script can be used to create a password for your `qBittorrent.conf`
file (placed in `.config/qbittorrent/qBittorrent.conf`).
"""
import base64
import hashlib


def pbkdf2_encode(password):
    salt = base64.b64decode('ARQ77eY1NUZaQsuDHbIMCA==')
    # Derive the key using PBKDF2-HMAC-SHA1
    key = hashlib.pbkdf2_hmac(
        'sha1',  # Hash algorithm
        password.encode('utf-8'),  # Convert password to bytes
        salt,  # Salt (bytes)
        iterations=10000,  # Number of iterations
        dklen=32  # Desired length of the derived key
    )
    # Encode the salt and key in Base64
    salt_b64 = base64.b64encode(salt).decode('utf-8')
    key_b64 = base64.b64encode(key).decode('utf-8')
    # Return the final string in the format "salt:key"
    encoded_password = f"{salt_b64}:{key_b64}"
    print('Place this under [Preferences] in your qBittorrent.conf file:')
    print(f'WebUI\Password_PBKDF2=@ByteArray({encoded_password})')
    return encoded_password


if __name__ == '__main__':
    # test example password out
    encoded_password = pbkdf2_encode(password='adminadmin')
