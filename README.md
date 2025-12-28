To run: Download NerdleEqns.txt: list of valid equations used by the game.
Run: python Nerdle-2.py

Instructions for gameplay:
Objective: Try to guess the 8 digit math equation.
For each guess, enter an equation that fills all 8 boxes using the following characters:
1234567890+-*/=. Press enter key to submit your guess.
For each character:
- If that character is correct and in the right place, its box will turn green.
- If that character is somewhere else in the equation, but not in the spot you
guessed, its box will turn yellow.
- If the character is nowhere in the equation, its box will stay black.

The game will only accept guesses that are mathematically correct. Additionally, it will
not accept a guess that is improperly formatted. Improper format means that there are two
operation symbols in a row (ex. 3++1+2=6 is not a valid guess). (This is also to avoid
python evaluating for exponents or integer division.) Also, if there is an operation symbol
somewhere after the equal sign, where the answer following it is a single number (ex.
43+4=+47 or 43+4=47+), that is invalid. In all these cases, if such an equation is entered,
nothing will happen. However, the game will accept answers that put the equal sign first
and the expression on the right (ex. 55=40+15), or two expressions on either side of the
equal sign (ex. 11+2=4*3), because those are still valid equations- but none of the
answers on the input list are formatted that way, so that answer will never be correct.
