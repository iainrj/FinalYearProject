import unittest
import support

class MyTest(unittest.TestCase):
    def testGetAdjacentNeighbour(self):
        self.assertEqual(support.getAdjacentNeighbour([0,1]), ([1,0],0))
        self.assertIsNot(support.getAdjacentNeighbour(['albania','russia','finland']), ['albania','russia','finland'])
        self.assertIsNot(support.getAdjacentNeighbour(['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany']), ['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany'])
    
    def testGetNeighbour(self):
        self.assertEqual(support.getNeighbour([0,1]), [1,0])
        self.assertIsNot(support.getAdjacentNeighbour(['albania','russia','finland']), ['albania','russia','finland'])
        self.assertIsNot(support.getAdjacentNeighbour(['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany']), ['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany'])

    def testRefinedMaxMin(self):
        scores = [0, 6, 1, 6, 10, 0, 17, 0, 7, 0, 20, 5, 20, 0, 4, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0, 0]
        solution = [47, 27, 23, 30, 47, 25, 75, 7, 18, 6, 140, 24, 119, 1, 22, 8, 8, 34, 39, 37, 63, 19, 42, 111, 1, 13, 47, 27, 23, 30, 47, 25, 75, 7, 18, 6, 140]
        j = 1
        self.assertEqual(support.refinedMaxMin(scores, solution, j, 12), 0)
        
        scores2 = [47, 27, 23, 30, 47, 25, 75, 7, 18, 6, 140, 24, 119, 1, 22, 8, 8, 34, 39, 37, 63, 19, 42, 111, 1, 13]
        j2 = 16
        self.assertEqual(support.refinedMaxMin(scores2, solution, j2, 12), 1)
        
        scores3 = [69, 28, 23, 51, 67, 48, 121, 7, 48, 12, 235, 24, 161, 1, 40, 21, 8, 55, 56, 55, 83, 23, 58, 169, 5, 29]
        j3 = 25
        self.assertEqual(support.refinedMaxMin(scores3, solution, j3, 12), 83)
        
if __name__ == '__main__':
    unittest.main()
