message_file = open("message_file.txt")

def decode(message_file):
	for cipher in message_file:
		cipher = message_file.readline()
		return cipher
	for code in cipher:
		code = cipher[-2]
		return code
	for msg in code:
		key.get(msg)
		return msg

key = {'6': 'computers', '3': 'love', '1': 'i'}

decode(message_file)

print(cipher)
print(code)
print(msg)
