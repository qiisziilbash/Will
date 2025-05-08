# My Digital Signature
I have a couple of close friends that have my secret key in case I die.

This is my public key (You can also find it in the `data/public_key.pem` file or my other genuine public profiles):

```
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiicaOmmFWUrD4zjrvBtl
HbdhavqMCFHhFzx0+TxyOOEMu3ejrU0hKlkrMpu4PeDK3Zfxo7q7gFRBUmlsQOxP
1K/K3+4zt6mMKRToNa++cqirgiloeyfNwdjHh/tU9ntvw0mPjuw6RvsUoF8FEikq
lldIXt9NQ8AjhiL5vKkRUkqsepfzdy4LZUgjy7vK9kvP3uhaZmYAMYeu59LGAuYI
hGJMzMBZMVt3FlPSmi/zI00sdjbbvfrNFasBfMynwkYNu+Sh3TNUv9LgNvgSneFk
63UHzi20K8UmWR9bzys2aDAQn6F18fYV4jOKW0S9zMZN4NbMzBA/BDd/IBCy256M
0QIDAQAB
-----END PUBLIC KEY-----
```

## How to install
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to decrypt my will
```bash
python decrypt.py will
```

## How to decrypt my passwords
```bash
python decrypt.py passwords
```

## How to verify my digital signature
1. Put the message to be claimed that is signed by me in the `data/message.txt` file
2. Put the signature hex in the `data/hex_signature.txt` file
3. Run
```bash
python verify.py
```