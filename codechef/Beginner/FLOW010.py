"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
URL: https://www.codechef.com/problems/FLOW010
 
Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.
 
Class ID	Ship Class
B or b	BattleShip
C or c	Cruiser
D or d	Destroyer
F or f	Frigate
 
*** Input ***
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains a character.
*** Output ***
Display the Ship Class depending on ID.
 
*** Constraints ***
1 <= T <= 1000
 
*** Example ***
 
Input
----
3 
B
c
D
Output
------
BattleShip
Cruiser
Destroyer
 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
DEBUG = False
 
def print_debug(s):
    if DEBUG: print str(s);
 
MAP = {
     'B': 'BattleShip'
    ,'C': 'Cruiser'
    ,'D': 'Destroyer'
    ,'F': 'Frigate'
     }
 
def translate(letter):
    return MAP[letter.upper()]
 
def run():
    print_debug('Number of entries:')
    lines = int(raw_input())
    while (lines > 0):
        print_debug("Entry in format '%c' as 'code'")
        code = raw_input()
        print '%s' % translate(code)
        lines = lines - 1;
    print_debug('Done')
 
if __name__ == "__main__":
    run()
 
