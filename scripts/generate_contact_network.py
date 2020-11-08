#! /usr/bin/env python3
'''
Generate a random contact network under the Barabasi-Albert (BA) model and output it in the GEMF format
'''
from networkx import barabasi_albert_graph
from sys import argv

# main content
if __name__ == "__main__":
    if len(argv) != 3:
        print("USAGE: %s <num_cn_nodes> <num_edges_from_new>" % argv[0]); exit(1)
    cn = barabasi_albert_graph(int(argv[1]), int(argv[2]))
    for edge in cn.edges():
        print('%s\t%s' % edge)
