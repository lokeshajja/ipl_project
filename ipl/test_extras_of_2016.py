import unittest
from file_extraction import extract_data
from extras_of_year_2016 import compute_extra_runs


delivery_data = extract_data('mock_deliveries_data.csv')


class TestExtraRunsConcededPerTeam2016(unittest.TestCase):

    def test_id_wise_data(self):
        inputs_and_outputs =\
         [((['594', '607', '631', '632', '633', '634', '635'], delivery_data),
             {'Sunrisers Hyderabad': 2, 'Gujarat Lions': 1,
              'Kolkata Knight Riders': 2, 'Delhi Daredevils': 5,
              'Royal Challengers Bangalore': 1})]
        for inputs, expected_output in inputs_and_outputs:
            output = compute_extra_runs(inputs[0], inputs[1])
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
