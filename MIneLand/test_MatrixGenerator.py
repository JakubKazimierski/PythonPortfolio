import unittest
import MatrixGenerator


class test_MatrixGenerator(unittest.TestCase):

    def test_ExpectedOutputLengths(self):
        #check if input data are equal to output data
        outputMatrix = MatrixGenerator.matrix(5,6)
        self.assertEqual(len(outputMatrix), 5)
    
        for i in range(0, len(outputMatrix)):
            self.assertEqual(len(outputMatrix[i]), 6)        

    def test_ExpectedValueRange(self):
        
        outputMatrix = MatrixGenerator.matrix(5,6)

        #as previous test is ok, all subtables in matrix are equal length
        #check if type is int
        # and check if range of values is correct    
        for i in range(0, len(outputMatrix)):
            for j in range(0, len(outputMatrix[i])):
                self.assertEqual(type(outputMatrix[i][j]), int)
                self.assertGreaterEqual(outputMatrix[i][j], 0)        
                self.assertLessEqual(outputMatrix[i][j], 1)

if __name__ == "__main__":
    unittest.main()