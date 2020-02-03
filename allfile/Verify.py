from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

massage = open("Team.txt","rb").read()
massage_digest = SHA256.new(massage)

signature = open("Digital_Signature.txt","rb").read()
key = RSA.importKey(open('public_key.pem').read())
verifier = PKCS1_v1_5.new(key)

if verifier.verify(massage_digest, signature):
   print ("The signature is authentic.")
else:
   print ("The signature is not authentic.")