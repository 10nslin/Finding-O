''' 
Scott Enslin
Write a program that takes a list of strings and a string containing a single character, 
and prints a new list of all the strings containing that character.
'''



word_list = ['hello','world','my','name','is','Anna']
newlist= []
char ="o"


for letter in word_list:
     if char in letter:
        newlist.append(letter)
        print(newlist)