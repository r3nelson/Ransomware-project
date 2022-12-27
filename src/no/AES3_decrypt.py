from Crypto.Cipher import AES 

'''
remember you have to change mode to be in save for decrypt.txt 
'''
with open('Save for decrypt.txt','rb') as f: # if we don't retrieve values of hkey, mode, iv, and file they  will be imported as the wrong (updated) value because of the time the file was run
    key_size = len(list(f.readline()))
    trash_line = f.readline() # need this line cause 2nd line is technically our \n (the empty line)
    # mode = len(list(f.readline(6))) # modes are saved as ints by AES. bytes will show how many ints. convert bytes to list and find len of list to see int value that corresponds to mode
    mode = 2
    iv = [f.readline()]
    iv = b'\xcc;\xfe\xf4\xd0e\xe9\xbez\xc5}\x86pc\x03\x9e'
    hkey = [f.readline()]
    # trash_line3 = f.readline()
    # hkey = [f.readline(key_size -1)]
    
print(f'key size is : {key_size}')
# print(trash_line)
print(f'mode is : {mode}')
# print(trash_line2)
print(f'iv is : {iv}')
# print(trash_line3)
print(f'hkey is : {hkey}')

def decrypt_file(): #make decryption function
    file = input('enter the name of the file you want decrypted:\n')
    with open(file,'rb') as f: # file is the file to be encrypted we defined above. 'rb' stands for read bytes
        not_original_file = f.read() # will read every line of the file
    if mode == AES.MODE_CTR:
        decipher = AES.new(hkey[0],mode)
    else:
        decipher = AES.new(hkey[0],mode,iv[0]) #standard notation for decryption is [encryption method used].new(key,mode,iv) key = hkey, mode= cbc, iv= iv
    pt=  decipher.decrypt(not_original_file) #pt stands for plaintext. Use the key, mode, and iv to decrypt the ciphertext into plaintext 
    with open(file, 'wb') as e:
        e.write(pt.rstrip(b'}')) #rstrip() to remove padding on file. If we don't remove padding the file will be corrupted
        
decrypt_file() # will execute our decrypt funtion and will create decrypted file