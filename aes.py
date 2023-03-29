from os import urandom
from Crypto.Cipher import AES


def Enc_AES (password , key , iv):
    # For Generating cipher text
    obj = AES.new(key, AES.MODE_CBC, iv)
    # Encrypt the message
    #print('Original message is: ', password)
    encrypted_text = obj.encrypt(password.encode('utf8'))
    #print('The encrypted password', encrypted_text)
    return encrypted_text

def Dec_AES (enc_password ,key, iv):
    # Decrypt the message
    rev_obj = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = rev_obj.decrypt(enc_password)
    print('The decrypted text', decrypted_text.decode('utf-8'))
    return  decrypted_text