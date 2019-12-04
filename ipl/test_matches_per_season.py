import unittest
from file_extraction import extract_data
from matches_played_per_year import compute_number_of_matches_played_per_year

mock_data = extract_data('matches.csv')
mock_matches = []
for mockdata in mock_data[:69]:
    mock_matches.append(mockdata)


class TestMatchesPerSeason(unittest.TestCase):

    def test_compute_number_of_matches_yearwise(self):

        inputs_and_outputs = [(mock_matches, {'2017': 59, '2008': 10})]
        for inputs, expected_output in inputs_and_outputs:
            output = compute_number_of_matches_played_per_year(inputs)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
