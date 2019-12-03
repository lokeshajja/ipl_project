import unittest
from file_extraction import extract_file
from extras_of_year_2016 import *





mock_data=extract_file('matches.csv')
count=0
mock_matches=[]
for mockdata in mock_data:
    if count<15:
        mock_matches.append(mockdata)
        count+=1


delivery_data=extract_file('deliveries.csv')
counts=0
mock_deliveries=[]
for ball_data in delivery_data:
    if counts<15:
        mock_deliveries.append(ball_data)
        counts+=1





class TestPlotData(unittest.TestCase):

    def test_id_wise_data(self):

        inputs_and_outputs=[((['1'],mock_deliveries),{'Royal Challengers Bangalore' : 4 }  )]
        for input,outputs in inputs_and_outputs:
            output = id_wise_data(input[0],input[1])
            self.assertEqual(output, outputs)





if __name__ == '__main__':
    unittest.main()
