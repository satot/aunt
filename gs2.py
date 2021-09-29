from collections import defaultdict
import unittest

def find_most_frequent(ips):
    iplist = [ip.split(" - ")[0] for ip in ips]
    counter = defaultdict(int)
    for ip in iplist:
        counter[ip] += 1
    max_value = max(counter.values())
    return [key for key, value in counter.items() if value == max_value]


# ---------------------------------- #
# Unit Test
# ---------------------------------- #
class TestFunc(unittest.TestCase):
    def test1(self):
        ips = [ 
          "10.0.0.1 - sample random text",
          "10.0.0.2 - another random text ",
          "10.0.0.3 - asdf ",
          "10.0.0.2 - adfafadsfs"
        ]
        self.assertEqual(find_most_frequent(ips), ['10.0.0.2'])

    def test2(self):
        ips = [ 
          "10.0.0.1 - sample random text",
          "10.0.0.2 - another random text ",
          "10.0.0.3 - asdf ",
          "10.0.0.2 - adfafadsfs",
          "10.0.0.3 - asdfafasf"
        ]
        self.assertEqual(find_most_frequent(ips), ['10.0.0.2', '10.0.0.3'])

    def test3(self):
        ips = [ 
          "10.0.0.1 - sample random text",
          "10.0.0.1 - sample random text",
          "10.0.0.1 - sample random text",
          "10.0.0.1 - sample random text"
        ]
        self.assertEqual(find_most_frequent(ips), ['10.0.0.1'])


if __name__ == '__main__':
    unittest.main()
