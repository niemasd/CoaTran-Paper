#! /usr/bin/env python3
'''
Randomly select sample times uniformly between time of infection and 2x time of last infection
'''
from random import uniform
from sys import argv

# main content
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <coatran_transmission_network>" % argv[0]); exit(1)
    inf_time = dict()
    for l in open(argv[1]):
        u,v,t = l.split('\t'); inf_time[v.strip()] = float(t)
    end = 2*max(inf_time.values())
    for u in inf_time:
        print("%s\t%f" % (u, uniform(inf_time[u],end)))
