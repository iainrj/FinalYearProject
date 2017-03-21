import unittest
import order

class MyTest(unittest.TestCase):
    def testGetAdjacentNeighbour(self):
        self.assertEqual(order.getAdjacentNeighbour([0,1]), [1,0])
        self.assertIsNot(order.getAdjacentNeighbour(['albania','russia','finland']), ['albania','russia','finland'])
        self.assertIsNot(order.getAdjacentNeighbour(['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany']), ['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany'])
    
    def testGetNeighbour(self):
        self.assertEqual(order.getNeighbour([0,1]), [1,0])
        self.assertIsNot(order.getAdjacentNeighbour(['albania','russia','finland']), ['albania','russia','finland'])
        self.assertIsNot(order.getAdjacentNeighbour(['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany']), ['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany'])

    def testRefinedMaxMin(self):
        scores = [0,0,1,2,3,5,7,8,10]
        solution = [0,0,1,2,3,5,7,8,10] # only used for length
        j = 0
        self.assertEqual(order.refinedMaxMin(scores, solution, j), 0)
        
        scores2 = [0,1,2,3,5,7,8,10,180]
        j2 = 3
        self.assertEqual(order.refinedMaxMin(scores2, solution, j2), 10)
        
        scores3 = [0,1,2,3,5,26,85,160,180]
        j3 = 5
        self.assertEqual(order.refinedMaxMin(scores3, solution, j3), 85)
        
if __name__ == '__main__':
    unittest.main()
