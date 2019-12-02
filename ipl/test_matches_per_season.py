import unittest
from file_extraction import extract_file
from matches_played_per_year import *

mock_data=extract_file('matches.csv')
cnt=0
mock_matches=[]
for mockdata in mock_data:
    if cnt<69:
        mock_matches.append(mockdata)
        cnt+=1



class TestMatch(unittest.TestCase):
    
    def test_compute_number_of_matches_yearwise1(self):

        inputs_and_outputs=[(mock_matches, {'2017': 59 , '2008' : 10})]
        for inputs,expected_output in inputs_and_outputs:
            output = compute_number_of_matches_yearwise(inputs)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()








