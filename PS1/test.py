#!/usr/bin/env python2.7
from parse import parse
import ID3
import unit_tests as tests

def main():
    e = parse("house_votes_84.data")
    ID3.split(e,len(e)-1)
    # f = ID3.ID3(e, 'empty')



if __name__ == "__main__":
    main()
