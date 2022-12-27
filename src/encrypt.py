from Crypto.Cipher import AES 
from Crypto.Hash import SHA256

def encrypt_file(file): # make encryption function
    with open('key.txt','rb') as f:
        hkey = f.read()

    with open('iv.txt','rb') as x:
        iv = x.read()
    with open(file, 'rb') as f: # file is the file to be encrypted we defined above. 'rb' stands for read bytes
        original_file = f.read()    # will read every line of the file
    BLOCK_SIZE = 16 # Block size is dependednt on encryption algorthim used for AES it is 16
    PAD = b'{' # the b is like the bytes version of the string. This will pad the file with "{" until it has symmetric block sizes of 16 bytes
    padding = lambda x: x + (BLOCK_SIZE-len(x) % BLOCK_SIZE) * PAD # will ensure the file is padded if it is not already in blocks of 16 bytes. See notes if this line does't make sense
    cipher= AES.new(hkey,AES.MODE_CBC,iv) #standard notation for encryption is [encryption method used].new(key,mode,iv) key = hkey, mode= cbc, iv= iv
    result = cipher.encrypt(padding(original_file)) # encrypt original file with padding. Techincally we are actually encrypting a copy of the original file. Might need to delete original file
    with open(file,'wb') as e: #create a file with same name as before plus encrypted and enable it to be editted
        e.write(result) # write result, which is our encyrption to our newly created file



    