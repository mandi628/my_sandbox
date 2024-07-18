# develop a function name 'decode(message_file)'. The 'message_file' argument is a string
# containing the file path for a .txt file that has an encoded message. When the function
# is called, it should read the file specified by its argument, decode the message, and
# return (not print) the decoded message as a string in a specific format,
    
# The key to decoding the message is to use the words corresponding to the numbers at the
# end of each pyramid line (in this example, 1, 3, and 6). The decoded message is formed by
# taking these words and separating them by individual spaces, with no extra characters. You
# should ignore all the other words.
key = {
	"1" : "i",
	"2" : "dogs",
	"3" : "love",
	"4" : "cats",
	"5" : "you",
	"6" : "computer"
}

message_file = open("message_file.txt")

def decode(message_file):
	for msg in message_file:
		print(msg[-2])


decode(message_file)
print(message_file)

message_file.close()

# 1. Read the message file
# 2. Pull the last character in each line of the message file
# 3. Look up the number in the key file
# 4. Return the corresponding word from the key file.