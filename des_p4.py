from Crypto.Cipher import DES 
from Crypto.Random import get_random_bytes 
import base64 
def main(): 
    message = input("Enter your message: ") 
    my_message = message.encode()  # String to byte array as DES works on bytes 
    key = get_random_bytes(8)  # DES key size should be 8 bytes (Generating Key) 
    # Initializing crypto algorithm 
    cipher = DES.new(key, DES.MODE_ECB) 
    # Setting encryption mode and encrypting 
    my_encrypted_bytes = cipher.encrypt(pad(my_message)) 
    # Setting decryption mode and decrypting 
    decrypted_cipher = DES.new(key, DES.MODE_ECB) 
    my_decrypted_bytes = unpad(decrypted_cipher.decrypt(my_encrypted_bytes)) 
    # Print message in byte format 
    encrypted_data = base64.b64encode(my_encrypted_bytes).decode() 
    decrypted_data = my_decrypted_bytes.decode() 
    print("Message : " + message) 
    print("Encrypted - " + encrypted_data) 
    print("Decrypted Message - " + decrypted_data) 
def pad(text): 
    # Padding to make the text length a multiple of 8 bytes (block size) 
    while len(text) % 8 != 0: 
        text += b' ' 
    return text 
def unpad(text): 
    # Removing padding 
    return text.rstrip(b' ') 
if __name__ == "__main__": 
    main()