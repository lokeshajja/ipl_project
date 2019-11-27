import unittest
from file_extraction import extract_file
from plot_of_task4 import *





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


class TestPlotData(unittest.TestCase):
    def test_economy_of_bowlers(self):
        bowler_data1={'UT Yadav': {'del': 60, 'runs': 40}, 'M Morkel': {'del': 120, 'runs': 100}, 'Shakib Al Hasan': {'del': 60, 'runs': 50}}
        ec_data={'UT Yadav': 4, 'M Morkel': 5, 'Shakib Al Hasan': 5 }
        inputs_and_outputs=[(bowler_data1,ec_data)]
        for input1,output1 in inputs_and_outputs:
            output = economy_of_bowlers(input1)
            self.assertEqual(output, output1)



if __name__ == '__main__':
    unittest.main()