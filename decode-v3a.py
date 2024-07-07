message_file = open("message_file1.txt")
#file = open(message_file)

msg = {'6': 'computers', '3': 'love', '1': 'i', '4': 'dogs', '2': 'cats', '7': 'and'}

def text():
	text = []
	for text in message_file:
		text = message_file.readlines()
		return text

def char():
	x = 0
	char = []
	while x < len(text):
		char.append(text[x][-2])
		x += 1
	return char

def decode(message_file):
	y = 0
	junk = []
	while y < len(char):
		junk.append(msg.get(char[y]))
		y += 1
	return junk
	close("message_file1.txt")

text = text()
print("Text = %s" % text)

char = char()
print("Characters = %s" % char)

junk = decode(message_file)
print(junk)
