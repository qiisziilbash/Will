# My Digital Signature
I have a couple of close friends that have my secret key in case I die.

This is my public key (You can also find it in the `data/public_key.pem` file or my other genuine public profiles):

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA6cbmsSk0S+fXAewUmt7O
HG6G52E8FKuuToUaJClXZEmedWE/Z2Tun9pconPMBRfATe3V52vngdIZ3hkohBtf
iELvlvLur0GwD4lzQ7YEkYKMXrfUpM3JUQ2OUzbGR33Q03+elgz58ysJUusToID5
DgomyWCaIg3Jwo5TPwxs/rBYgFVUD/XPkd83OoWZzumHsa6cs93vq7wV9BtYJ5hC
tv/aJ7htOLCpY6RggfCvcy2DJl4b6znsInfgnLgQhntrh/gSycgpfk5Lc/RW5BUa
eSY7kMs6dXE02m1WxJqA0DeN0mKcXHAebHXGNkFOTTWw5jHgeEB+BljaAsth+fKZ
4wIDAQAB
-----END PUBLIC KEY-----
```

## How to install
This is tested on Python 3.11.0 and 3.13.3

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to decrypt my will
Note that you need the private key to decrypt.
Please put the private key in the `data/private_key.pem` file and then run:

```bash
python decrypt.py will
```

## How to decrypt my passwords
Note that you need the private key to decrypt.
Please put the private key in the `data/private_key.pem` file and then run:

```bash
python decrypt.py passwords
```

## How to verify my digital signature
1. Put the message to be claimed that is signed by me in the `data/message.txt` file
2. Put the signature hex in the `data/hex_signature.txt` file
3. Run:

    ```bash:
    python verify.py
    ```