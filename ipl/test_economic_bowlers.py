import unittest
from file_extraction import extract_data
from most_econ_bowlers_2015 import calculate_economy_of_bowlers


mock_data = extract_data('matches.csv')
mock_matches = []
for mockdata in mock_data[:15]:
    mock_matches.append(mockdata)

delivery_data = extract_data('deliveries.csv')
mock_deliveries = []
for ball_data in delivery_data[:15]:
    mock_deliveries.append(ball_data)


class TestMostEconomicBowlers(unittest.TestCase):

    def test_calculate_economy_of_bowlers(self):

        bowler_data = {'UT Yadav': {'balls': 60, 'runs': 40}, 'M Morkel':
                       {'balls': 120, 'runs': 100}, 'Shakib Al Hasan':
                       {'balls': 60, 'runs': 50}}
        economy_data = {'UT Yadav': 4, 'M Morkel': 5,
                        'Shakib Al Hasan': 5}
        inputs_and_outputs = [(bowler_data, economy_data)]

        for inputs, expected_output in inputs_and_outputs:
            output = calculate_economy_of_bowlers(inputs)

            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
