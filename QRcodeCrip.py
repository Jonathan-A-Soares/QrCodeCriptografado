import jwt
import json
import random
import string
import base64
import qrcode

KeyDefalt = "Alfa2X2~6K9#%NçU1~3Q2S9U3Q7A4ç3C3GçC7#%W6T"

def RandomCode():
    carA = "rgg"
    carN = "grf"
    key = "Alfa" 
    key1 = "rpvo"

    for item in range(1,20):
        carA = random.choice(string.ascii_uppercase)
        carN = random.randrange(1, 10)
        carN = str(carN)
        key1 = carN+ carA
        key = key + key1
    return key

def CripSha256(key,code):
    encoded = jwt.encode({
        "msg":code
    }, key, algorithm="HS256")
    return encoded

def CripSha2562Key(key1,key,code):
    encoded = jwt.encode({
        "msg":code,
        "key": key1
    
    }, key, algorithm="HS256")
    return encoded

def CripBase64(msg):

    message = msg
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    return base64_message
#geral key randomica
KeyRandom = RandomCode()
#criptografa pastel com key randomica
CodeSha = CripSha256(KeyRandom,"pastel")
#criptografa key usada para criptografar pastel
KeyBase64Crip = CripBase64(KeyRandom)
#criptografa pastel com key criptografada em base64 com key defalt do progama
KeyEnd = CripSha2562Key(KeyBase64Crip,KeyDefalt,CodeSha)

filename = "Confidencial.png"
img = qrcode.make(KeyEnd)
img.save(filename)
print(KeyEnd)

