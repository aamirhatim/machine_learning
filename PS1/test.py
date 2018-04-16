#!/usr/bin/env python2.7
from parse import parse
import ID3

def main():
    e = parse("house_votes_84.data")
    # print len(e)
    f = ID3.ID3(e, 0)
    # print len(e[0].keys())-1

    # h = ID3.H(4, 2, 6)
    # print h

if __name__ == "__main__":
    main()
