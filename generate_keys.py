# %%
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


public_prefix = "mario"  # use "" if you want to generate a random key


def generate_key_with_prefix(desired_prefix):
    while True:
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())

        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        b64_str = base64.b64encode(public_pem).decode("utf-8")
        if b64_str.startswith(desired_prefix):
            return private_key, public_key


private_key, public_key = generate_key_with_prefix(public_prefix)

private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("private_key.pem", "wb") as file:
    file.write(private_pem)

with open("public_key.pem", "wb") as file:
    file.write(public_pem)
