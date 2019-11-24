from matches_played_per_year import compute_and_plot_matches_played_per_year
from file_extraction import extract_file
from number_of_matches_won_by_each import matches_won_by_each
import os
import sys
import numpy as np



deliveries_data=extract_file('deliveries.csv')
#print(deliveries_data)
#sample data structure inside the deliveries data
''' ('636', '2', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', '20', '6', '
Iqbal Abdulla', 'Sachin Baby', 'B Kumar', '0', '0', '0', '0', '0',
 '0', '4', '0', '4', '', '', '') '''

matches=extract_file('matches.csv')
#print(matches[0])


year_and_id={}
years=[]
for match in matches[1:]:
    if match[1] not in year_and_id:
        year_and_id[match[1]]=[match[0]]

    elif match[1] in year_and_id:
        (year_and_id[match[1]]).append(match[0])

    else:
        pass

#print(year_and_id)
''' '2016': ['577', '578', '579', '580', '581', '582', '583', '584', '585', '586', '587',
 '588', '589', '590', '591', '592', '593', '594', '595', '596', '597', '598', '599', 
 '600', '601', '602', '603', '604', '605', '606', '607', '608', '609',
'610', '611', '612', '613', '614', '615', '616', '617', '618', '619', '620', '621', 
'622', '623', '624', '625', '626', '627', '628', '629', '630', '631', '632', '633', 
'634', '635', '636']'''
#sample data structure

matches_of_2k16=year_and_id['2016']
#print(matches_of_2k16)


match_id_data={}

for match_id in deliveries_data[1:]:

    if match_id[0] in match_id_data:
        match_id_data[match_id[0]].append(match_id[1:])

    elif match_id[0] not in match_id_data:
        match_id_data[match_id[0]]=[]
        match_id_data[match_id[0]].append(match_id[1:])
    else:
        pass 

#print(len(match_id_data['636'])//6)
#total overs played can be guessed
#sample data structure of id wise data
''' ('2', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad', '20', '6', 'Iqbal Abdulla', 
'Sachin Baby', 'B Kumar', '0', '0', '0', '0', '0', '0', '4', '0', '4', '', '',
'')]'''





#print(match_id_data)         # only last delivery data is getting saved**                 

#extra runs index = 15 

extra_runs_data={}
for ids in matches_of_2k16:
    #print(ids)
    extra_runs=match_id_data[str(ids)]
    batting_team=match_id_data[str(ids)][1]
    bowling_team=match_id_data[str(ids)][2]
    #print(extra_runs)
    #print(bowling_team)
    #print(batting_team)

    '''#if bowling_team == 'Rising Pune Supergiants' or bowling_team == 'Rising Pune Supergiant' :
       # bowling_team='Rising Pune Supergiants'
    
    if batting_team=='Rising Pune Supergiants' or batting_team == 'Rising Pune Supergiant':
       batting_team='Rising Pune Supergiants'

    else:
        pass


    if  extra_runs_data[batting_team] in extra_runs_data:
        extra_runs_data[batting_team]+=extra_runs

    elif extra_runs_data[batting_team] not in extra_runs_data:
        extra_runs_data[batting_team]=extra_runs

    else:
        pass'''


#print(extra_runs_data)











