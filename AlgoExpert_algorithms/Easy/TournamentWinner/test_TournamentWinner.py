'''
Unittests for TournamentWinner.py
February 2021 Jakub Kazimierski
'''

import unittest
from TournamentWinner import tournamentWinner

class test_TournamentWinner(unittest.TestCase):    
    '''
    Class with unittests for TournamentWinner.py
    '''

    def setUp(self):
        '''
        Sets up input.
        '''
        self.input_list = [
                        ['HTML', 'C#'],
                        ['C#', 'Python'],
                        ['Python', 'HTML'],
                    ]
        self.input_results = [0, 0, 1]

        self.output = 'Python'
        return self.input_list, self.input_results, self.output

    # region Unittests
    def test_ExpectedOutput(self):
        '''
        Checks if returned output is as expected.
        '''
        input_list, input_results, output = self.setUp()
        output_method  = tournamentWinner(input_list, input_results)
        self.assertEqual(output, output_method)
   # endregion

if __name__ == "__main__":
    '''
    Main method for test cases.
    '''
    unittest.main()