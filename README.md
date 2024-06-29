# git_test
My first GitHub repo!
Hello Odin!

----------

Changed repo name to "my_sandbox" to make a place for my learning space.

----------

SAMPLE PROJECT:

Coding Job - app.dataannotation.tech

Part 3 - Coding Exercise: Decoding a Message from a Text File

In this exercise, you will develop a function name 'decode(message_file)'. The 'message_file' argument is a string containing the file path for a .txt file that has an encoded message. When the function is called, it should read the file specified by its argument, decode the message, and return (not print) the decoded message as a string in a specific format, described below.

Note that you can write your code using any language and IDE you want (Python is preferred if possible, but no mandatory).

Your function must be able to process an input file with the following format:

3 love
6 computer
2 dogs
4 cats
1 i
5 you

In this file, each line contains a number followed by a word. The task is to decode a hidden message based on the arrangement of these numbers into a "pyramid" structure. The numbers are placed into the pyramid in ascending order, with each line of the pyramid having one more number than the line above it. The smallest number is 1, and the numbers increase consecutively, like so:

1
2 3
4 5 6

The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (in this example, 1, 3, and 6). The decoded message is formed by taking these words and separating them by individual spaces, with no extra characters. You shoul ignore all the other words. So for the example input file above, the message words are:

1: i
3: love
6: computers

and your function would return the string "i love computers".

Please submit the complete code for the decode function:

Explain how your code works in 2-3+ complete sentences.
