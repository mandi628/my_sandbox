message_file = open("message_file.txt")

msg = list()

def cipher():
	for cipher in message_file:
		cipher = message_file.readlines()
		return cipher

cipher_list = cipher()
print(cipher_list)

def code(cipher_list):
	if cipher_list != " ":
		return cipher_list[-2]

code = code(cipher_list)
print(code)

#def decode(message_file):
#	for cipher in message_file:
#		cipher = message_file.readline()
#		return cipher
#	for code in cipher:
#		code = cipher[-2]
#		return code
#	for msg in code:
#		key.get(msg)
#		return msg
#
#key = {'6': 'computers', '3': 'love', '1': 'i'}
#
#decode(message_file)
#
#close("message_file.txt")
#
#print(code)
#print(msg)
