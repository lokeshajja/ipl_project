import unittest
from file_extraction import extract_file
from number_of_matches_won_by_each import *


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
    if cnt1<50:
        mock_deliveries.append(mockdata1)
        cnt1+=1

#print(mock_deliveries)




class TestMatchWon(unittest.TestCase):
    def test_matches_won_by_each(self):
        inputs_and_outputs=[(mock_matches, {'2017': {'Sunrisers Hyderabad': 2, 'Rising Pune Supergiants': 1, 'Kolkata Knight Riders': 3, 'Kings XI Punjab': 2, 'Royal Challengers Bangalore': 1, 'Mumbai Indians': 3, 'Delhi Daredevils': 2, 'Gujarat Lions': 1}})]
        for input1,output1 in inputs_and_outputs:
            output = matches_won_by_each(input1)
            self.assertEqual(output, output1)











if __name__ == '__main__':
    unittest.main()
