from twofish import Twofish

def tfencrypt(plaintext, password):

    bs = 16 #block size 16 bytes or 128 bits 
 
    if len(plaintext)%bs: #add padding 
        padded_plaintext=str(plaintext+'%'*(bs-len(plaintext)%bs)).encode('utf-8')
    else:
        padded_plaintext=plaintext.encode('utf-8')
    
    T = Twofish(str.encode(password))
    ciphertext=b''

    for x in range(int(len(padded_plaintext)/bs)):
         ciphertext += T.encrypt(padded_plaintext[x*bs:(x+1)*bs])
    

    return ciphertext


def tfdecrypt(ciphertext, password):

    bs = 16 #block size 16 bytes or 128 bits
    T = Twofish(str.encode(password))
    plaintext=b''

    for x in range(int(len(ciphertext)/bs)):
        plaintext += T.decrypt(ciphertext[x*bs:(x+1)*bs])
        
    text=str.encode(plaintext.decode('utf-8').strip('%'))
    return text

