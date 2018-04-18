#!/usr/bin/env python2.7
from parse import parse
import ID3
import unit_tests as tests

def main():
    e = parse("house_votes_84.data")
    training, validation = ID3.split(e,435)

    f = ID3.ID3(training, 'empty')
    print ID3.test(f, training)
    print ID3.test(f, validation)



if __name__ == "__main__":
    main()
