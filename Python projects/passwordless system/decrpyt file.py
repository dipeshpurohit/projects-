from cryptography.fernet import Fernet


key = Fernet.generate_key()

with open('key.key', 'wb') as mykey:
    mykey.write(key)


with open('key.key', 'rb') as mykey:
    key = mykey.read()

print(key)
f = Fernet(key)

with open('userdata.txt', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_userdata.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

f = Fernet(key)

with open('enc_userdata.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_userdata.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file, encrypted_file):
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file, decrypted_file):
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, 'wb') as file:
            file.write(decrypted)


encryptor=Encryptor()

mykey=encryptor.key_create()

encryptor.key_write(mykey, 'key.key')

loaded_key=encryptor.key_load('key.key')

encryptor.file_encrypt(loaded_key, 'userdata.txt', 'enc_userdata.txt')

encryptor.file_decrypt(loaded_key, 'enc_userdata.txt', 'dec_userdata.txt')