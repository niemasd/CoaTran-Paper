#! /usr/bin/env python3
'''
Convert a GEMF transmission network to the CoaTran format
'''
from random import choice
from sys import argv

# main content
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <GEMF_output>" % argv[0]); exit(1)
    for i,l in enumerate(open(argv[1])):
        t = l.split()[0].strip()
        u = l.split()[2].strip()
        v = choice(l.split()[-1].replace('[','').replace(']','').strip(',').strip().split(',')).strip()
        if i == 0:
            print("None\t%s\t0" % u) # seed
        print('%s\t%s\t%s' % (u,v,t))
