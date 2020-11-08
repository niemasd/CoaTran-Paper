#! /usr/bin/env python3
'''
Convert a CoaTran sample times to the VirusTreeSimulator format
'''
from sys import argv

# main content
if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: %s <coatran_samples_tsv>" % argv[0]); exit(1)
    print("IDPOP,TIME_SEQ,SEQ_COUNT")
    for l in open(argv[1]):
        u,t = [x.strip() for x in l.strip().split('\t')]
        print('%s,%s,1' % (u,t))
