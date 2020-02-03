from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import hashlib

message = open("Team.txt","rb").read()
key = RSA.importKey(open('private_key.pem').read())
message_digest = SHA256.new(message)
signer = PKCS1_v1_5.new(key)
digital_signature = signer.sign(message_digest)
open("Digital_Signature.txt","wb").write(digital_signature)