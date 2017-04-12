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
        
    # def testOffsetGetEntertainment(self):
    #     xNow = ['albania','russia','finland','france','italy','spain','romania','germany']
    #     countries = ['albania','russia','finland']
    #     score_board = [
    #         [ 0,  0,  5, 10,  8,  4,  1,  8],
    #         [ 0,  8,  0,  7,  0,  0,  0,  0],
    #         [ 0,  0,  0,  0,  3,  0,  0,  0]
    #     ]
    #     voters = ['albania','russia','finland', 'france', 'italy', 'spain', 'romania', 'germany'],
    #     key1 = 4,
    #     oldEntertainment = ,
    #     oldDistances = []
        
    #     self.assertEqual(order.offsetGetEntertainment(), 4124)
    
    # def testCalculateDistances(self):
    #     score_board = [
    #         [ 0,  5,  5, 5, 5],
    #         [ 1,  0,  3, 1, 0],
    #         [ 5,  3,  0, 3, 3],
    #         [ 3,  1,  1, 0, 1]
    #     ]    
    #     #         al  ru  fi  fr es
    #     #     al [ 0,  5,  5, 5, 5],
    #     #     ru [ 1,  0,  3, 1, 0],
    #     #     fi [ 5,  3,  0, 3, 3],
    #     #     it [ 3,  1,  1, 0, 1]
    #     solution = ['albania','russia','finland','france', 'spain']
    #     voters = ['albania','russia','finland', 'france', 'spain']
    #     performers = ['albania','russia','finland', 'italy']
    #     no_performers = len(performers)
        
    #     self.assertEqual(order.calculateDistances(solution, voters, no_performers, score_board), [5, 8, 10, 15, 6])
        
if __name__ == '__main__':
    unittest.main()
