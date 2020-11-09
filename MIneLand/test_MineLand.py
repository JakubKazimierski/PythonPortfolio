import unittest
import MineLand
import MatrixGenerator

class test_MineLand(unittest.TestCase):

    def test_ExpectedOutput(self):
        output = MineLand.MineLand(MatrixGenerator.matrix(5,4), [1,2])
        self.assertEqual(output, 1)

    def test_WrongData(self):
        output = MineLand.MineLand(MatrixGenerator.matrix(5,4), [11,2])
        self.assertEqual(output, -1)

if __name__ == "__main__":
    unittest.main()        