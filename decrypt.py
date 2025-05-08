# %%
import sys

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

folder_name = sys.argv[1] if len(sys.argv) > 1 else "message"

# %%
with open(f"data/{folder_name}/hex_encrypted_content.txt", "r") as file:
    encrypted_message = file.read()
    encrypted_message = bytes.fromhex(encrypted_message)
with open(f"data/{folder_name}/hex_encrypted_aes_key.txt", "r") as file:
    encrypted_aes_key = file.read()
    encrypted_aes_key = bytes.fromhex(encrypted_aes_key)
with open(f"data/private_key.pem", "rb") as file:
    private_key_data = file.read()
    private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())

# %%
aes_block_size = 16  # AES block size in bytes - messages must be padded to be a multiple of this
decrypted_aes_key = private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None),
)

decryptor = Cipher(
    algorithms.AES(decrypted_aes_key), modes.CBC(encrypted_message[:aes_block_size]), backend=default_backend()
).decryptor()
decrypted_padded = decryptor.update(encrypted_message[aes_block_size:]) + decryptor.finalize()
pad_len = decrypted_padded[-1]
plaintext = decrypted_padded[:-pad_len]

print("Decrypted message:", plaintext.decode())


# %%
