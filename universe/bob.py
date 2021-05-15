from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import PyPDF2
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

file = open('12.pdf', 'rb')
fileread = PyPDF2.PdfFileReader(file)
getpage = fileread.getPage(0)
text_file = getpage.extractText()
#імпортуємо публічний ключ
with open("key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
    )

text_file = bytes(text_file, 'utf-8')

with open("sign_1.txt", "rb") as signa:
    signature = signa.read()

public_key.verify(
    signature,
    text_file,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
