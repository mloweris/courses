import sys
import os

srcdir = os.getcwd() + '/src'
sys.path.append(srcdir)

import hw

def main():
    outdir = os.getcwd() + '/out'
    testlog = open(outdir + '/tests.log', 'w+')

    score = 0
    feedback = 'you\'re awesome!!!'

    term = 'random'

    if not hasattr(hw, 'frequency'):
        feedback = 'frequency undefined' 
    elif hw.frequency(term):
        score = 1

    print(str(score) + ';' + feedback, file=testlog)
    testlog.close()

main()