import unittest
from file_extraction import extract_file
from most_econ_bowlers_2015 import economy_of_bowlers


mock_data = extract_file('matches.csv')
count = 0
mock_matches = []
for mockdata in mock_data:
    if count < 15:
        mock_matches.append(mockdata)
        count += 1


delivery_data = extract_file('deliveries.csv')
serial = 0
mock_deliveries = []
for ball_data in delivery_data:
    if serial < 15:
        mock_deliveries.append(ball_data)
        serial += 1


class TestPlotData(unittest.TestCase):

    def test_economy_of_bowlers(self):

        bowler_data = {'UT Yadav': {'balls': 60, 'runs': 40}, 'M Morkel':
                       {'balls': 120, 'runs': 100}, 'Shakib Al Hasan':
                       {'balls': 60, 'runs': 50}}
        economy_data = {'UT Yadav': 4, 'M Morkel': 5,
                        'Shakib Al Hasan': 5}
        inputs_and_outputs = [(bowler_data, economy_data)]
        for inputs, expected_output in inputs_and_outputs:
            output = economy_of_bowlers(inputs)
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
