python-wordle-cli

Command line game based on wordle classic.
It is a 5 letter wordle classic.
Guess the WORDLE in six tries.
Each guess must be a valid five-letter word. Hit the enter button to submit.
  Capital Letters are letters in the correct location
  Lowercase Letters are within the word, but not the correct location
  
Demo with 4 letters
-----------------Rules-------------------

Capital Letters are letters in the correct location
Lowercase Letters are within the word, but not the correct location
-------------------------------------------------------------------
bloke
6 Tries left. Enter a valid 5 letter word: rught
Invalid input <rught>.
6 Tries left. Enter a valid 5 letter word: right

----Game Board----
*****
*****
*****
*****
*****
*****

----Key Board-----
q w e * * y u * o p
a s d f * * j k l
z x c v b n m
5 Tries left. Enter a valid 5 letter word: right

----Game Board----
*****
*****
*****
*****
*****
*****

----Key Board-----
q w e * * y u * o p
a s d f * * j k l
z x c v b n m
4 Tries left. Enter a valid 5 letter word: crate

----Game Board----
*****
*****
****E
*****
*****
*****

----Key Board-----
q w E * * y u * o p
* s d f * * j k l
z x * v b n m
3 Tries left. Enter a valid 5 letter word: meets

----Game Board----
*****
*****
****E
*ee**
*****
*****

----Key Board-----
q w e * * y u * o p
* * d f * * j k l
z x * v b n *
2 Tries left. Enter a valid 5 letter word: moron

----Game Board----
*****
*****
****E
*ee**
*o*o*
*****

----Key Board-----
q w e * * y u * o p
* * d f * * j k l
z x * v b * *
1 Tries left. Enter a valid 5 letter word: loops

----Game Board----
*****
*****
****E
*ee**
*o*o*
loO**

----Key Board-----
q w e * * y u * O *
* * d f * * j k l
z x * v b * *

No more tries. The word was "BLOKE"
