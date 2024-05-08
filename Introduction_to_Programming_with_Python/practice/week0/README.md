## Creating Code with VS Code
In Terminal type
```
code hello.py
```
In hello.py type
```
print("hello, world")
```
In Terminal type
```
python hello.py
```
Output in Terminal
```
hello, world
```
## Functions
- functions are action that computer or language knows to perform
- in ``hello.py`` ``print()`` is a function to perform print in terminal
## Bugs
- bugs are mistake that a programmer or user perform which misplace action of the code
Example
- in hello.py if we type
```
print("hello, world"
```
and try to run with 
```
pyton hello.py
```
bug output as ``SyntaxError``
## improving ``hello.py``
using ``input()`` function to take user input 
```
input("What's your name? ")
print("hello, world")
```
still if we run this it will ask for input but print ``hello, world`` only
## Variables
it just a container to store value ``x=1`` here x is variable and 1 is value
editing ``hello.py``
```
# variable = value
name = input("What's your name? ")
print("hello,")
print(name)
```
for more information on [data type](https://docs.python.org/3/library/datatypes.html) python documentation
## Comments
notes on source code for the programmer for themself or other to explain
in ``hello.py``
```
# starting with (#) is a comment in python
# variable = value
# ask user for their name
name = input("What's your name? ")

# greet user with name
print("hello,")
print(name)
```
now when running the source code
```
python hello.py
```
output as
```
what's your name? Ranjit
hello,
Ranjit
```
## Psudocode
using comment as a todo list or code to be implimented
in ``hello.py``
```
# ask user for their name using input
name = input("What's your name? ")

# greet user with hello and their name
# with print function
print("hello,")
print(name)
```
## improving ``hello.py``
```
# ask user for name
name = input("What's your name? ")
# greet user 
print("hello,", name)
```
output as ``hello, user_name`` here , provide two argument to print function ``hello,`` and ``name``
also , provide space in between the argument
```
# ask user for name
name = input("What's your name? ")
# greet user 
print("hello, "+ name)
```
output is same but here we pass one argument after the string is joined(concatinate) with ``+`` and space is manually placed
## string and parameters
python document on string [(str)](https://docs.python.org/3/library/stdtypes.html#str) and [print](https://docs.python.org/3/library/functions.html#print)
in ``print()`` we have some parameters as ``end="\n"`` or ``sep=" "`` which is print new line at end and seperate the given argument
with space 
