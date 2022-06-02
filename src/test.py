# import required module
from cryptography.fernet import Fernet
import base64
from Crypto.Cipher import AES
# obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')

# message = "Python is fun"
# message_bytes = message.encode('unicode')
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('unicode')

#'boaenc-802834679,h4XViZ/knQLbGTncXIxcaT4ovEVGIzw6/j/JEXL0D5lxsr9yV++nGDkZHbX2bKgT9kCdgXnToXHaBd5I3vv13Wxw4NApY2HhLU4mNt4b/Vs='
#key= b"nGDkZHbX2bKgT9kCdgXnToXHaBd5I3vv13Wxw4NApY2HhLU4mNt4b/Vs="
key = "0x05A275A67A042591D114C0E29552AD743C2A1DD507228C17E2788A4F708D1DDF8F88A1AA33F33108604A1B9BF9DBB896344C54DD7A0CA42D752D6E25C4783AA4D69F60E89130FB034B9304910D334312324B587FCC36607373DB54DC3F4826C09E1EC398EDE0D772845E03CE889BBCD9D792C537362DD2D09B0CF46D35B29811"
message_bytes = key.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
encryptedStr = 'boaenc-802834679,h4XViZ/knQLbGTncXIxcaT4ovEVGIzw6/j/JEXL0D5lxsr9yV++nGDkZHbX2bKgT9kCdgXnToXHaBd5I3vv13Wxw4NApY2HhLU4mNt4b/Vs='
#key = Fernet.generate_key()

fernet = Fernet(message_bytes)
decrypted = fernet.decrypt(encryptedStr)
print(decrypted)
# aes = AES.new(key, AES.MODE, 'This is an IV456')
# decd = aes.decrypt(encryptedStr)
# print(decd)

# # opening the key
# filekey = open('key.txt', 'rb')
# key = filekey.read()
# print(key)
# # using the key
# fernet = Fernet(key)
# # print(fernet)
# # decrypting the file
# decrypted = fernet.decrypt(encryptedStr)
