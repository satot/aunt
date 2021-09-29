test = [
    ["Charles", 100],
    ["John", 69],
    ["James", 50],
    ["Charles", 20]
]

from collections import defaultdict

def avg(ls):
    return sum(ls)/len(ls)

def find_highest(d):
    aggr = defaultdict(list)
    for name, score in d:
        aggr[name].append(score)
    return max([avg(x) for x in aggr.values()])
    

#print(find_highest(test))

import unittest

class TestCase(unittest.TestCase):
    def test1(self):
        test = [
            ["Charles", 100],
            ["John", 69],
            ["James", 50],
            ["Charles", 20]
        ]
        self.assertEqual(find_highest(test), 69)

    def test2(self):
        test = [
            ["Charles", 100],
            ["John", 69],
            ["James", 50],
            ["John", 19],
            ["Charles", 20]
        ]
        self.assertEqual(find_highest(test), 60)

    def test3(self):
        test = [
            ["John", 60],
            ["James", 60],
            ["Charles", 20]
        ]
        self.assertEqual(find_highest(test), 60)

if __name__ == '__main__':
    unittest.main()        
