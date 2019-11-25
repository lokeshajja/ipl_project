from file_extraction import extract_file
import os
import sys
import numpy as np

#matches=extract_file('matches.csv')
#print(matches[0])




def matches_won_by_each(matches):

    winners_data={}
    for winner in matches[1:]:
        winners=winner[10]
        if winners=='Rising Pune Supergiant':
            winners='Rising Pune Supergiants'



        if winners in winners_data:
            winners_data[winners]+=1
        elif winners not in winners_data:
            winners_data[winners]=1
        else:
            pass

    return winners_data


    
    








#print(matches_won_by_each(matches))

