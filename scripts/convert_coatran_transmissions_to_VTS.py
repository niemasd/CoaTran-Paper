#! /usr/bin/env python3
'''
Convert a CoaTran transmission network to the VirusTreeSimulator format
'''
from sys import argv

# main content
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <coatran_transmissions_tsv>" % argv[0]); exit(1)
    print("IDREC,IDTR,TIME_TR")
    for l in open(argv[1]):
        u,v,t = [x.strip() for x in l.strip().split('\t')]
        if u == 'None':
            u = 'NA'
        print('%s,%s,%s' % (v,u,t))
