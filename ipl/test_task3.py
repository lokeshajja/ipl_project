import unittest
from file_extraction import extract_file
from extras_of_year_2016 import *





mock_data=extract_file('matches.csv')
cnt=0
mock_matches=[]
for mockdata in mock_data:
    if cnt<15:
        mock_matches.append(mockdata)
        cnt+=1

mock_data1=extract_file('deliveries.csv')
cnt1=0
mock_deliveries=[]
for mockdata1 in mock_data1:
    if cnt1<15:
        mock_deliveries.append(mockdata1)
        cnt1+=1

#print(mock_deliveries)



class TestPlotData(unittest.TestCase):
    def test_id_wise_data(self):
        inputs_and_outputs=[((['1'],mock_deliveries),{'Royal Challengers Bangalore' : 4 }  )]
        for input1,output1 in inputs_and_outputs:
            output = id_wise_data(input1[0],input1[1])
            self.assertEqual(output, output1)











if __name__ == '__main__':
    unittest.main()
