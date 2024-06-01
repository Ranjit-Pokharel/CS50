## Computer Science
Computer programming, outpu solution by input of problem and in between a program that convert it.

``input => [program] => output``
computer use binary system ``0 and 1``
millions and billions of tiny transistors being on (1) and off (0)
```example how computer counts
000 = 0
001 = 1
010 = 2
011 = 3
100 = 4
101 = 5
110 = 6
111 = 7
4th place 3th place 2nd place 1st place
uses base-2 to count
2^2 2^1 2^0
```
computer use 8-bits or 1-byte to represent number 00000000 = 0 and 11111111 = 255

## ASCII
![](./extra/ascii.png)
letters are represented using 0 and 1
``A`` = 65 (01000001)
```
72 = H
73 = I
33 = !
```

## Unicode
are other special charecter and emoji that are use for communication

## Colors
Red, Green, Blue (RGB)
represent as intensity of this colors
```
r  g  b
72 73 33 gives light shade of yellow
```
image are the collection of RGB values
videos are collection of changing images

## Sound
represented with MIDI data

## Algorithms
```finding single name in phone book
maximum speed of the algorithms = big-O notation
step to fing the name = nth step (n)
1. single page at a time = n steps
2. two pages at a time = n/2 steps (with fix of some bug)
3. go to the middle of the phone book and ask, 
“Is the name I am looking for to the left or to the right?” Then, repeat this process, 
cutting the problem in half and half and half. = log2 n
```
![](./extra/time_vs_size_of_problem.png)
this all are algorithms

## Pseudocode
pseudocode is human readable version of code
```pseudocode of contact book (algorithms)
1.pick up phone book
2.open middle of phone book
3.look at the page
4.if person is on the page
5.  call person
6.else if person is earlier of book
7.  open to middle left of half of book
8.  go back to line 3
9.else if person is later of book
10. open to middle right of half of book
11. go back to line 3
12.else
13. quit
```
pseudocode helps in 2 ways
- think logical to problem in advance
- help to understand the code

## Artifical Intelligence
```sample AI chat bot pseudocode
1.if say hello
2.  say hello back
3.else if say goodbye
4.  say goodbye back
5.else if say how are you
6.  say i am well, what about you
7.........
```
simple conversation takes large number of lines
``Large Language Modles (LLM)`` looks for pattern in a huge block of language
Such language models attempt to create a best guess of what words come after one another or alongside one another.

## Scratch
visual programming language developed my mit
### practice
- [Hello, World](https://scratch.mit.edu/projects/1030514017)
