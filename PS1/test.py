#!/usr/bin/env python2.7
from parse import parse
import ID3
import unit_tests as tests

def main():
    e = parse("house_votes_84.data")
    # print len(e)
    f = ID3.ID3(e, 'empty')
    for i in range(10):
        print ID3.evaluate(f,e[i])
    print ID3.test(f, e)

    # tests.testID3AndEvaluate()
    # tests.testID3AndTest()

    # data = [dict(a=1, b=0, Class=2), dict(a=1, b=1, Class=1),
    #         dict(a=2, b=0, Class=2), dict(a=2, b=1, Class=3),
    #         dict(a=3, b=0, Class=1), dict(a=3, b=1, Class=3)]
    # tree = ID3.ID3(data, 0)


if __name__ == "__main__":
    main()
