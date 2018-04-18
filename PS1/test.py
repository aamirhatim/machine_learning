#!/usr/bin/env python2.7
from parse import parse
import ID3

def main():
    e = parse("house_votes_84.data")
    # print len(e)
    f = ID3.ID3(e, 'empty')
    # for i in range(10):
    #     print ID3.evaluate(f,e[i])
    ID3.test(f, e)


if __name__ == "__main__":
    main()
