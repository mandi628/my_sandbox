message_file = open("message_file.txt")

msg = list()

def cipher():
	for cipher in message_file:
		cipher = message_file.readlines()
		return cipher

cipher_list = cipher()
print(cipher_list)

def code():
	for code in cipher_list:
		x = 0
		while x < len(cipher_list):
			return cipher_list[x][-2]
		x += 1

code = code()
print(code)

key = {'6': 'computers', '3': 'love', '1': 'i'}

def decode(message_file):
	for msg in code:
		msg = code()
		key.get(msg)
		return msg

decode(message_file)

close("message_file.txt")

print(msg)
