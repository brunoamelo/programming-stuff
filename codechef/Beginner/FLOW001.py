"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

URL: https://www.codechef.com/problems/FLOW001

Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.
Program is very simple, Given two integers A and B, write a program to add these two numbers. 

*** Input ***
The first line contains an integer T, total number of test cases. Then follow T lines, each line contains two Integers A and B.

*** Output*** 
Add A and B and display it.

*** Constraints*** 
1 <= T <= 1000
1 <= A,B <= 10000

*** Example ***

Input
-----
3 
1 2
100 200
10 40

Output
------
3
300
50

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

DEBUG = False

def print_debug(s):
    if DEBUG: print str(s);

def run():
    print_debug('Number of entries:')
    lines = int(raw_input())
    while (lines > 0):
        print_debug("Entry in format '%f %f' as 'A B'")
        [a, b] = [int(s) for s in raw_input().split(' ')];
        print '%d' % (a+b)
        lines = lines - 1;
    print_debug('Done')

if __name__ == "__main__":
    run()

