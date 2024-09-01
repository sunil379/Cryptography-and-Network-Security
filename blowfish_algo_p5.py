from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

class BlowfishDemo:
    def encrypt(self, password, key):
        key_bytes = key.encode('utf-8')
        cipher = Blowfish.new(key_bytes, Blowfish.MODE_ECB)
        padded_password = pad(password.encode('utf-8'), Blowfish.block_size)
        encrypted_bytes = cipher.encrypt(padded_password)
        encrypted_text = base64.b64encode(encrypted_bytes).decode('utf-8')
        return encrypted_text

    def decrypt(self, encrypted_text, key):
        key_bytes = key.encode('utf-8')
        cipher = Blowfish.new(key_bytes, Blowfish.MODE_ECB)
        encrypted_bytes = base64.b64decode(encrypted_text)
        decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), Blowfish.block_size)
        decrypted_string = decrypted_bytes.decode('utf-8')
        return decrypted_string

if __name__ == "__main__":
    password = input("Enter the password: ")
    key = input("Enter the key: ")
    
    obj = BlowfishDemo()
    
    enc_output = obj.encrypt(password, key)
    print("Encrypted text:", enc_output)
    
    dec_output = obj.decrypt(enc_output, key)
    print("Decrypted text:", dec_output)
    
# Output :
# Enter the password: GCOEN Mihan
# Enter the key: knowledgefactory
# Encrypted text: XDBeURqdkV1MdK/INgGs7g==
# Decrypted text: GCOEN Mihan