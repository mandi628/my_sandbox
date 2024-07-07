message_file = open("message_file.txt")

msg = list()

def cipher():
	for cipher in message_file:
		cipher = message_file.readlines()
		return cipher

cipher = cipher()
print(cipher)

def code():
	x = 0
	while x < len(cipher):
		return cipher[x][-2] #When I use "print" in this line, I get what I'm looking for, but "return" only gives me one reponse.
		x += 1

code = code()
print(code)

msg = {'6': 'computers', '3': 'love', '1': 'i', '4': 'dogs', '2': 'cats'}

print(msg)

msg1 = (code[0])
msg2 = (code[1])
msg3 = (code[2])
#print(msg.get(msg1))
#print(msg.get(msg2))
#print(msg.get(msg3))

#def decode(message_file):
#	for msg in code:
#		msg = code()
#		key.get(msg)
#		return msg

#decode(message_file)

#close("message_file.txt")

#print(msg)
