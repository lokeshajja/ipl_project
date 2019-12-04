import unittest
from file_extraction import extract_data
from number_of_matches_won_by_each import\
    matches_won_by_each_team_over_all_seasons


mock_data = extract_data('matches.csv')
count = 0
mock_matches = []
for mockdata in mock_data:
    if count < 15:
        mock_matches.append(mockdata)
        count += 1


delivery_data = extract_data('deliveries.csv')
serial = 0
mock_deliveries = []
for ball_data in delivery_data:
    if serial < 50:
        mock_deliveries.append(ball_data)
        serial += 1


class TestMatchWon(unittest.TestCase):

    def test_matches_won_by_each(self):

        inputs_and_outputs = [(mock_matches,
                               {'2017': {'Sunrisers Hyderabad': 2,
                                         'Rising Pune Supergiants': 1,
                                         'Kolkata Knight Riders': 3,
                                         'Kings XI Punjab': 2,
                                         'Royal Challengers Bangalore': 1,
                                         'Mumbai Indians': 3,
                                         'Delhi Daredevils': 2,
                                         'Gujarat Lions': 1}})]
        for inputs, expected_output in inputs_and_outputs:
            output = matches_won_by_each_team_over_all_seasons(inputs)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
