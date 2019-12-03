import unittest
from file_extraction import extract_file
from max_centuries import *





mock_data=extract_file('matches.csv')
count=0
mock_matches=[]
for mockdata in mock_data:
    if count<5:
        mock_matches.append(mockdata)
        count+=1


delivery_data=extract_file('deliveries.csv')
serial=0
mock_deliveries=[]
for delivery in delivery_data:
    if serial<15:
        mock_deliveries.append(delivery)
        serial+=1


class TestPlotData(unittest.TestCase):
    def test_ids_of_each_year(self):
        yr_data={ '2017' : {} }
        op={ '2017' : { '1' : {} , '2' : { }, '3' : {} , '4' : {} , '5' : { }} }
        inputs_and_outputs=[((yr_data,mock_matches),op)]
        for input1,output1 in inputs_and_outputs:
            output = ids_of_each_year(input1[0],input1[1])
            self.assertEqual(output, output1)


if __name__ == '__main__':
    unittest.main()