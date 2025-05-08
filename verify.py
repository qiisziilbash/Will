# %%
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# %%
with open("data/public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

with open("data/message/content.txt", "rb") as message_file:
    message = message_file.read()

with open("data/message/hex_signature.txt", "r") as signature_file:
    signature = signature_file.read()
    signature = bytes.fromhex(signature)

try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256(),
    )
    print("Signature is valid!")
except Exception as e:
    print("Signature verification failed!")
    print(f"Error: {e}")

# %%
