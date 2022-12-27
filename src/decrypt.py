from Crypto.Cipher import AES 
from Crypto.Hash import SHA256

def decrypt_file(cipher_text): #make decryption function
    with open('key.txt','rb') as f:
        hkey = f.read()
    with open('iv.txt','rb') as x:
        iv = x.read()
    with open(cipher_text,'rb') as f: # file is the file to be encrypted we defined above. 'rb' stands for read bytes
        not_original_file = f.read() # will read every line of the file
    decipher = AES.new(hkey,AES.MODE_CBC,iv) #standard notation for decryption is [encryption method used].new(key,mode,iv) key = hkey, mode= cbc, iv= iv
    pt = decipher.decrypt(not_original_file) #pt stands for plaintext. Use the key, mode, and iv to decrypt the ciphertext into plaintext 
    with open(cipher_text, 'wb') as e:
        e.write(pt.rstrip(b'}')) #rstrip() to remove padding on file. If we don't remove padding the file will be corrupted
        
# plaintext = decrypt_file(cipher_text) # will execute our decrypt funtion and will create decrypted file