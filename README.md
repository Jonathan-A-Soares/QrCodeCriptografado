# Documentação para o Código de Criptografia e QR Code

## Visão Geral

Este código Python demonstra a geração de uma chave aleatória, a criptografia de uma mensagem e a criação de um código QR contendo a chave final. A chave final inclui a mensagem criptografada, a chave original e a chave codificada em base64.

## Bibliotecas Utilizadas

- `jwt`: Usada para criar tokens JSON Web.
- `json`: Usada para lidar com dados JSON.
- `random`: Usada para gerar números e caracteres aleatórios.
- `string`: Usada para manipular caracteres alfanuméricos.
- `base64`: Usada para codificar e decodificar em base64.
- `qrcode`: Usada para criar códigos QR.

## Funções Principais

1. `RandomCode()`: Gera uma chave aleatória composta por letras maiúsculas e números. A chave gerada é usada como parte da criptografia.

2. `CripSha256(key, code)`: Cria um token JWT (JSON Web Token) usando o algoritmo de criptografia HS256 (HMAC-SHA-256). O token contém uma mensagem (`code`) e é assinado com uma chave (`key`). O token criptografado é retornado.

3. `CripSha2562Key(key1, key, code)`: Similar à função anterior, mas também inclui uma segunda chave (`key1`) no token. Esta função cria um token JWT que contém a mensagem (`code`) e duas chaves diferentes (`key` e `key1`) e é assinado com a chave `key`.

4. `CripBase64(msg)`: Codifica uma mensagem em base64.

## Uso do Código

O código pode ser usado para gerar uma chave criptografada que pode ser usada para descriptografar uma mensagem posteriormente. A chave final é codificada em um código QR para fácil compartilhamento.

## Exemplo de Uso

```python
# Geração de uma chave aleatória
KeyRandom = RandomCode()

# Criptografia da palavra "pastel" usando a chave aleatória
CodeSha = CripSha256(KeyRandom, "pastel")

# Codificação da chave aleatória em base64
KeyBase64Crip = CripBase64(KeyRandom)

# Criação de uma chave final
KeyEnd = CripSha2562Key(KeyBase64Crip, KeyDefalt, CodeSha)

# Criação de um código QR com a chave final
filename = "Confidencial.png"
img = qrcode.make(KeyEnd)
img.save(filename)
print(KeyEnd)
