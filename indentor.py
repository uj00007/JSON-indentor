#!/usr/bin/python3
with open("raw.txt") as input_file:
    text = input_file.read()
istack = [] #creating an empty list and the list is appended for calculation of spaces
str_length = 0 #for calculating temporary string length
indent = 0     #for calculation for idents or spaces after which line has to come and initializing it currently at the start with 0
current_string = ""   #for calculating the string to be printed
text = text.replace("\n{", "{")    #for replacing \n{ if by chance the raw text contains it with {
for char in text:
    if char == '\n':      #if code contains \n printing the current string calculated till \n and reset the str_length
        print(current_string)
        current_string = " " * indent  #initializing the current string again with the spaces currently in that indent
        str_length = 0
    elif not (char == '{' or char == '}' or char == '[' or char == ']' or char == ','):
        #if the raw text contains anythng other than  { } [ ] ,
        str_length += 1  #increasing the temporrary str_len
        current_string += char   #calculating current string
    elif char == '}' or char == ']': #if } or ] appears printing the calculated current string
        print(current_string)
        current_string = " " * indent   #initializing the current string again with spaces so that to indent again
        print(current_string + char)     #then printing } with indentation
        indent = istack.pop()             #updating the indentation value by popping out from isstack
        current_string = " " * indent     #updating the current string by again initializing the current string with spaces required for indentation
        str_length = 0          #resetting the temporary string length with 0 for the calculating the next temporary string length
    elif char == '{' or char == '[':  #if raw text contains { or [
        istack.append(indent)         #pushing into the list the indent value currently
        indent = str_length + istack[-1]   #updating the indent value with current temporary string length + list value
        print(current_string + char)      #printing the combined current string with {
        current_string = " " * indent #updating the current string by again initializing the current string with spaces required for indentation
        str_length = 0           #resetting the temporary string length with 0 for the calculating the next temporary string length
    elif char == ',':  #when , comes in raw text
        print(current_string + char)  #print the current string with ,
        current_string = " " * indent #updating the current string by again initializing the current string with spaces required for indentation
        str_length = 0   #resetting the temporary string length with 0 for the calculating the next temporary string length
