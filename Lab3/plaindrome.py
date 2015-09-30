#Read in input from user
a = input("What word would you like to check\n")
a = a.lower()

#line to reverse the string that has been read in and saved as new string
reverse_word = a[::-1]
 
#checking if original string and reversed string are the same
if reverse_word == a:
#true printed if string is a palindrome
	print(True)
else:
#false printed if string is not  a palindrome
	print(False)
