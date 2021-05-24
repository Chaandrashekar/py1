Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s
NameError: name 's' is not defined
'
>>> s="10010"
>>> c=int(s,2)
>>> print("after converting integer to base of 2 value:%d"%c,end="/n")
after converting integer to base of 2 value:18/n
>>> print("after converting integer to base of 2 value:%d"%c,end="\n")
after converting integer to base of 2 value:18
>>> e=float(s)
>>> print("after converting int to float %f"%e,end="\n")
after converting int to float 10010.000000
>>> s='4'
>>> c=ord
(
>>> c=ord(s)
>>> print("after converting string value into int value:"%c)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print("after converting string value into int value:"%c)
TypeError: not all arguments converted during string formatting
>>> print("after converting string value into int value:%c"%c)
after converting string value into int value:4
>>> c=hex(56)
>>> print("after converting 56 to hex:"+c)
after converting 56 to hex:0x38
>>> s='edureka'
>>> c=tuple(s)
>>> print("after converting string into tuple :"c)
SyntaxError: invalid syntax
>>> print("after converting string into tuple :",c)
after converting string into tuple : ('e', 'd', 'u', 'r', 'e', 'k', 'a')
>>> c=set(s)
>>> print("after converting string into set:",c)
after converting string into set: {'k', 'r', 'u', 'e', 'd', 'a'}
>>> c=list(s)
>>> print("after converting string into lists:",c)
after converting string into lists: ['e', 'd', 'u', 'r', 'e', 'k', 'a']
>>> a=1
>>> b=2
>>> tup=(('a',1),('b',2),('g',3))
>>> c=complex(1,2)
>>> print("after converting int into complex number:",%c)
SyntaxError: invalid syntax
>>> print("after converting int into complex number:",c)
after converting int into complex number: (1+2j)
>>> c=str(a)
>>> print("after converting int into string:",c)
after converting int into string: 1
>>> c=dict(tup)
>>> print("after converting tuple to dictionary:",c)
after converting tuple to dictionary: {'a': 1, 'b': 2, 'g': 3}
>>> print("hello,World,Python!)
      
SyntaxError: EOL while scanning string literal
>>> print("hello,World,Python!")
hello,World,Python!
>>> 