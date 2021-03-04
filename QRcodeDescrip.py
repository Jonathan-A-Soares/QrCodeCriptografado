import jwt
import json
import random
import string
import base64
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
KeyDefalt = "Alfa2X2~6K9#%NçU1~3Q2S9U3Q7A4ç3C3GçC7#%W6T"

def LeQrcode():
    filename = "Confidencial.png"
    img = Image.open(filename)
    result = decode(img)
    for i in result:
       tght = i.data.decode("utf-8")
       test =""
       tet= test + tght
    return tet

def decriptSha256(code,key):
    decoded = jwt.decode(code,key, algorithms=["HS256"])
    return decoded

def descripbase64(cripmsg):

    base64_message = cripmsg
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message


#le Qrcode
descrip1 = LeQrcode()
#descriptografa o conteudo dele
descrip2 = decriptSha256(descrip1,KeyDefalt)
#separa a so a criptografia da msg
code = descrip2['msg']
#separa key de descriptografia da msg
keyBase64 = descrip2['key']
#descriptografa a key que esta em base64
keydecript = descripbase64(keyBase64)
#pega key com mensagem criptografada e descriptografa
codeEnd = decriptSha256(code,keydecript)
print(codeEnd['msg'])



