message_file = open("message_file.txt")

msg = {'6': 'computers', '3': 'love', '1': 'i', '4': 'dogs', '2': 'cats'}

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

def decode(message_file): # ? Would this still work if I didn't have the "message_file" parameter here?
	y = 0
	junk = []
	while y < len(char):
		junk.append(msg.get(char[y]))
		y += 1
	return junk
	close("message_file.txt")

text = text()
print("Text = %s" % text)

char = char()
print("Characters = %s" % char)

junk = decode(message_file)
print(junk)

#z = 0
#while z < len(junk):


# I noticed one tiny flaw. When reading the text file in the text(), it is starting with line 2 of the file, instead of line 1. Is that an indexing thing?
