# %%
import base64

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# %%
with open("data/private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

with open("data/message.txt", "rb") as message_file:
    message = message_file.read()

signature = private_key.sign(
    message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256()
)

# %%
with open("data/hex_signature.txt", "w") as signature_file:
    signature_file.write(signature.hex())

# %%
