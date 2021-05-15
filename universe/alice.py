from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import PyPDF2

private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=2048,)
#читаємо файл
file = open('12.pdf', 'rb')
fileread = PyPDF2.PdfFileReader(file)
getpage = fileread.getPage(0)
text_file = getpage.extractText()

#генеруємо публічний ключ з приватного
public_key = private_key.public_key()
pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

pem.splitlines()

file = open("key.pem", "wb")
file.write(pem)
file.close()

text_file = bytes(text_file, 'utf-8')
#підписуємо файл
signature = private_key.sign(
    text_file,
    padding.PSS(
       mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

file = open("sign_1.txt", "wb")
file.write(signature)
file.close()
