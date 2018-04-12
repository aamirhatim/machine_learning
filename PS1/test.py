#!/usr/bin/env python2.7
from parse import parse

def main():
    e = parse("house_votes_84.data")
    print e[0]

if __name__ == "__main__":
    main()
