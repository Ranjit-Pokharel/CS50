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
``
what's your name? Ranjit
hello,
Ranjit
``
