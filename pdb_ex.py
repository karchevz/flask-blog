import sys
from random import choice
import pdb

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
    print "To exit this game type 'exit'"

    a  = choice(random1)
    b = choice(random2)

    #pdb.set_trace()

    answer = raw_input("What is {} times {}? : ".format(a,b))
    
    #exit
    if answer == "exit":
        print "Now exiting game!"
        sys.exit()

    # determine f number is correct
    elif answer == str(a*b):
        print "Correct!"
    else:
        print "Wrong!"
