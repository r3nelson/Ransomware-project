import os
# import subprocess
# import json

# def check_permissions(*args):
#     for file in args:
#         permissions = ''
#         if os.access(file, os.R_OK) == True:
#             permissions+= 'r'
#         if os.access(file, os.W_OK) == True:
#             permissions+= 'w'
#         if os.access(file, os.X_OK) == True:
#             permissions+= 'x'
#         print(f'{file} : {permissions}')

# l = ['key.txt','wolf.png','poop.docx','extra.txt']
# check_permissions(*l)


# def rm(*args):
#     for file in args:
#         if os.path.exists(file):
#             print(f'removing {file}')
#             os.remove(file)
#         else:
#             print(f"The file {file} cannot be removed because it does not exist")

# l = ['extra.txt']
# rm(*l)

# def mkdir(dir):
#     parent_path = os.getcwd()
#     path = os.path.join(parent_path, dir)
#     os.mkdir(path)
#     print(f'created directory {dir} in {parent_path}')

# mkdir('test')

# command = input('enter a command\n')
# p1 = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
# result = f'stdout: {p1.stdout}\nstderr: {p1.stderr}'
# print(result)

# x = """{
#     "Name": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "Email": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
#     }"""

# y = json.loads(x)
  
# # the result is a Python dictionary:
# print(y)

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        # if encrypt_or_decrypt == 'encrypt':
        try:
            # encrypt_file(os.path.join(root, name))
            print(f'file: {os.path.join(root, name)}')
        except PermissionError:
            print(f'need elevated permissions: {os.path.join(root, name)}')
            continue
        except:
            continue