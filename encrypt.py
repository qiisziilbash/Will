# %%
import os
import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

folder_name = sys.argv[1] if len(sys.argv) > 1 else "message"
# %%
with open(f"data/{folder_name}/content.txt", "r") as file:
    message = file.read()
    message = bytes(message, "utf-8")
with open("data/public_key.pem", "rb") as file:
    public_key_data = file.read()
    public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())


# %%
aes_block_size = 16  # AES block size in bytes - messages must be padded to be a multiple of this
random_init_vector = os.urandom(aes_block_size)  # Prepend this to encrypted message so receiver can decrypt
aes_key = os.urandom(32)  # Using AES-256 which requires a 32 byte (256 bit) key
encryptor = Cipher(algorithms.AES(aes_key), modes.CBC(random_init_vector), backend=default_backend()).encryptor()

pad_len = aes_block_size - (len(message) % aes_block_size)
padded_message = message + bytes([pad_len] * pad_len)
encrypted_message = encryptor.update(padded_message) + encryptor.finalize()

# %%
encrypted_aes_key = public_key.encrypt(
    aes_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# %%
with open(f"data/{folder_name}/hex_encrypted_content.txt", "w") as file:
    file.write((random_init_vector + encrypted_message).hex())

with open(f"data/{folder_name}/hex_encrypted_aes_key.txt", "w") as file:
    file.write(encrypted_aes_key.hex())
