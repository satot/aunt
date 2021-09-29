import unittest

def find_common(array: list) -> str:
    ans = array[0] if len(array) > 0 else ""
    for w in array:
        j = 0
        while j < min([len(ans), len(w)]):
            if w[j] == ans[j]:
                j += 1
            else:
                break
        ans = "".join(w[:j])
    return ans

class TestFunc(unittest.TestCase):
    def testcase1(self):
        test = [
            'company',
            'community',
            'computer',
        ]
        self.assertEqual(find_common(test), 'com')

    def testcase2(self):
        test = [
            'add',
            'adjective',
            'additional',
        ]
        self.assertEqual(find_common(test), 'ad')

    def testcase3(self):
        test = [
        ]
        self.assertEqual(find_common(test), '')

    def testcase4(self):
        test = [
            'abc'
        ]
        self.assertEqual(find_common(test), 'abc')

    def testcase5(self):
        test = [
            '',
            'abce'
        ]
        self.assertEqual(find_common(test), '')

if __name__ == "__main__":
    unittest.main()
