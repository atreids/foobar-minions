import solution
import unittest

class Test_TestSolution(unittest.TestCase):
    def testCase1(self):
        self.assertListEqual(solution.solution([1,2,3], 0), [])
    def testCase2(self):
        self.assertListEqual(solution.solution([1,2,2,3,3,4,5,5], 1), [1,4])
    def testCase3(self):
        self.assertListEqual(solution.solution([1,1,1,5,5,5,5,5,5,2,3,2,1,4,1], 5), [1,1,1,2,3,2,1,4,1,])
    def testCase4(self):
        self.assertListEqual(solution.solution([100,32,100,2,2,100,5,6,100], 2), [32,2,2,5,6])

if __name__ == '__main__':
    print("----------------------------------------------------------")
    unittest.main()
    