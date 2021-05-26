my_string="All the tech company are good"
print(my_string)
print(type(my_string))#check what is the data type of my variable
print(len(my_string))#prints the size of the string
print(my_string[0:5])#prints elements upto 5 in sting
print(my_string[:5])#prints elements upto 5 in a string
print(my_string[0:78])#here the python interpreter assumes that you asked the max amount present in your string when you give string values above string range
print(my_string[::-1])#here this inverese the string
print(my_string[::55586])#here the value at 0th position in kept and the interpreter finds the element 55587 in my string
print(my_string[0:7:3])#here the elments upto 6th position are used and 2 char are skipped
print(my_string[::])#here all the char of my string will be printed
print(my_string.isalnum())#checks that a string is numerical or not
print(my_string.isalpha())#check that a string is alpha or not
print(my_string.endswith('good'))#here in check for last word in a string
print(my_string.count('o'))#here is counts the number of element of a spec., letter in a string
print(my_string.lower())#here we convert all the char in the string function as lower case
print(my_string.upper())#here we convert all the char in the string function as upper case
print(my_string.replace("good","best"))#here  we replace as char in a string of a function with anyother values from the user
