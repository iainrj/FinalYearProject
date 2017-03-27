import unittest
import order

class MyTest(unittest.TestCase):
    def testGetAdjacentNeighbour(self):
        self.assertEqual(order.getAdjacentNeighbour([0,1]), ([1,0],0))
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
    
    def testCalculateDistances(self):
        score_board = [
            [ 0,  5,  5, 5, 5],
            [ 1,  0,  3, 1, 0],
            [ 5,  3,  0, 3, 3],
            [ 3,  1,  1, 0, 1]
        ]    
        #         al  ru  fi  fr es
        #     al [ 0,  5,  5, 5, 5],
        #     ru [ 1,  0,  3, 1, 0],
        #     fi [ 5,  3,  0, 3, 3],
        #     it [ 3,  1,  1, 0, 1]
        solution = ['albania','russia','finland','france', 'spain']
        voters = ['albania','russia','finland', 'france', 'spain']
        performers = ['albania','russia','finland', 'italy']
        no_performers = len(performers)
        
        self.assertEqual(order.calculateDistances(solution, voters, no_performers, score_board), [5, 8, 10, 15, 6])
        
if __name__ == '__main__':
    unittest.main()
