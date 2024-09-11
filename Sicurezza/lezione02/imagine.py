from Crypto.Cipher import AES
import base64

# Function to pad the message to be multiple of 16 bytes
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Encryption
def encrypt(plain_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad(plain_text).encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Decryption
def decrypt(encrypted_text, key):
    cipher = AES.new(pad(key).encode('utf-8'), AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8').strip()
    return decrypted_text

# Example usage
key = "ThisIsASecretKey"
plain_text = "Hello, World!"
encrypted_text = encrypt(plain_text, key)
decrypted_text = decrypt(encrypted_text, key)

print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)

import base64

riga = input("Inserire una stringa: ")
print("Riga letta: ", riga)

riga_b64 = base64.b64encode(riga.encode("utf-8"))
print("Riga base64: ", riga_b64.decode("utf-8"))

riga_decoded = base64.b64decode(riga_b64)
print("Riga decoded: ", riga_decoded.decode("utf-8"))



# prova di decifra brute force
enc = "OgJuOYJZT0FDb47DBOkNgA=="
key = "XXXXIsASecretKey"

for p1 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p2 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        for p3 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            for p4 in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                key = p1 + p2 + p3 + p4 + "IsASecretKey"
                try:
                    dec = decrypt(enc, key)
                    print("La chiave è: ", key, " e la stringa è: ", dec)
                except:
                    # continua
                    continue


def LeggiBinario(pin, pout):
    with open(pin, mode="rb") as fin:
        with open(pout, mode="w") as fou:
            dati = fin.read()
            for v in dati:
        
                fou.write(str(v))
                fou.write("\n")


def ScriviBinario(tin, tou):
    with open(tin, mode="r") as fin:
        with open(tou, mode="wb") as fou:
            nums = fin.readlines()
            for num in nums:
                a = int(num).to_bytes()
                fou.write(a)


# esempio
LeggiBinario("pitone.jpeg", "pitone.txt")
ScriviBinario("pitone.txt", "pitone1.jpeg")
