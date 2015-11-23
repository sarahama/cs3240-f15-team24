import base64
import os
import sys
from Crypto.Cipher import AES

def encrypt(key, plaintext, iv):
	if len(iv) < 16:
		while len(iv) < 16:
			iv += 'X'
	if len(key) < 16:
		while len(key) < 16:
			key += 'X'
	mod16 = len(plaintext) % 16
	if mod16 != 0:
		while ((len(plaintext) % 16) != 0):
			plaintext += 'X'
	encobj = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = encobj.encrypt(plaintext)
	return ciphertext

def decrypt(key, ciphertext, iv):
	if len(iv) < 16:
		#print ("test")
		while len(iv) < 16:
			iv += 'X'
	if len(key) < 16:
		#print ("test")
		while len(key) < 16:
			key += 'X'
	decobj = AES.new(key, AES.MODE_CBC, iv)
	plaintext = decobj.decrypt(ciphertext)
	return plaintext