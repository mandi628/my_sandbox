astring = "Hello, World!"
print("single quotes are ' '")

print(astring)

characters = len(astring)
print("# characters: %s" % characters)

oh = astring.index("o")
print("place of 1st o: %s" % oh)

el = astring.count("l")
print("# of l's: %s" % el)

slice1 = astring[3:7]
print("slice no. 1: %s" % slice1)

#If you just have one number in the brackets, it will give you the single character at that index. If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in. If you leave out the second number, it will give you a slice from the first number to the end.

slice2 = astring[:7]
print("slice no. 2, 7 to end: %s" % slice2)

slice3 = astring[3:]
print("slice no. 3, beg to index 3: %s" % slice3)
