import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode


class AESCipher(object):
    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = key_file.encode()
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

# -----INITIALIZATION-----
# Ask for the user's choice: 1 for encryption, 2 for decryption
choice = int(input('Enter:\n1 for Encryption\n2 for Decryption\n'))

if choice == 1:
    file_name = input('Enter a file name: ')
# -----ENCRYPTION-----
# Open the file to be encrypted in the code
    file = open(file_name, 'r')
# Assign the file to be encrypted to a variable
    data = file.read()
    file.close()
# Generate a key to encrypt with
    enc = AESCipher(data)
# Use the key to generate the encrypted the file
    enc_file = open(f'encrypted-{file_name}', 'w')
    enc_file.write(enc.encrypt(data))
    enc_file.close()
        # f.write(cipher)
# Write the key value to a new file
    keygen_decoded = enc.key.decode('utf-16')
    with open(f'key-{file_name}', 'w', encoding = 'utf-16') as g:
        g.write(keygen_decoded)

# -----DECRYPTION-----
elif choice == 2:
    file_input = input('Enter an encrypted file name: ')
    key_file = input('Enter the key file name: ')

    file = open(file_input, 'r')
    data = file.read()
    file.close()

    file2 = open(key_file, 'r', encoding = 'utf-16')
    data2 = file2.read()
    file2.close()

    enc = AESCipher(data)
    dec_file = open(f'decrypted-{file_input}', 'w')
    dec_file.write(enc.decrypt(data, data2))
    dec_file.close()
# Open the encrypted file in the code
# Assign the encrypted file to a variable
# Take the file containing the generated key as an argument
# Use the key file to decrypt the encrypted file
# Return the decrypted file

