message_file = open("message_file.txt")

msg = list()

#print(message_file.readlines())

def cipher():
	for cipher in message_file:
		cipher = message_file.readlines()
		return cipher

cipher = cipher()
print(cipher)

def code():
	x = 0
	code = []
	while x < len(cipher):
		code.append(cipher[x][-2])
		x += 1

code = code()
print(code)

#msg = {'6': 'computers', '3': 'love', '1': 'i', '4': 'dogs', '2': 'cats'}

#print(msg)

#msg1 = (kode[0])
#msg2 = (kode[1])
#msg3 = (kode[2])
#print(msg.get(msg1))
#print(msg.get(msg2))
#print(msg.get(msg3))

#def decode(message_file):
#	for msg in kode:
#		msg = kode()
#		key.get(msg)
#		return msg

#decode(message_file)

#close("message_file.txt")

#print(msg)
