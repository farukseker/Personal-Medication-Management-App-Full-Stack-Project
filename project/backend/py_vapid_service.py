# pip install cryptography base64

import base64
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# VAPID Keypair üret
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

# 🔒 Backend'te saklanacak Private Key (PEM)
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# 📤 Client tarafına verilecek Public Key (raw → base64-url)
raw_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.X962,
    format=serialization.PublicFormat.UncompressedPoint
)

# base64-url encode + padding kaldır
vapid_public_key_b64url = base64.urlsafe_b64encode(raw_public_key).decode("utf-8").rstrip("=")

print("🔐 Private Key (PEM):\n", private_pem.decode())
print("📤 Public Key (Base64 URL):\n", vapid_public_key_b64url)
