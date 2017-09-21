import getpass
import subprocess

__all__ = [encrypt, decrypt]

def getNcheckPass():
	passwd = getpass.getpass("Enter the password: ")

	return passwd

def encStatus(file_path):
	with open(file_path, mode="rt") as fh:
		for i, aLine in enumerate(fh):
			if " " in aLine:
				return "not-encrypted"
			elif i > 100:
				return "not-encrypted"
	return "encrypted"

def encrypt(file_path):
	return

def decrypt(file_path):
	return
