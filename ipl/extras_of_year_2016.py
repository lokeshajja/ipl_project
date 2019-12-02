
from file_extraction import extract_file
import os
import sys
import numpy as np
from matplotlib import pyplot as plt



def year_and_id_data(matches):
    matches_of_2016=[]
    
    for match in matches:
        #print(match)
        if match['season'] =='2016':
            matches_of_2016.append(match['id'])

    #print(matches_of_2016)

    return matches_of_2016








def id_wise_data(matches_of_2016,deliveries_data) :
    ids=matches_of_2016
    teams_and_extra_runs={}
    for d_data in deliveries_data:
        if d_data['match_id'] in ids:
            if d_data['bowling_team'] not in teams_and_extra_runs:
                teams_and_extra_runs[d_data['bowling_team']]=int(d_data['extra_runs'])
            elif d_data['bowling_team'] in teams_and_extra_runs:
                teams_and_extra_runs[d_data['bowling_team']]+=int(d_data['extra_runs'])
    print(teams_and_extra_runs)
    
    return teams_and_extra_runs


def plotting_data():
    matches=extract_file('matches.csv')
    matches_of_2016=year_and_id_data(matches)
    #print(matches_of_2016)

    deliveries_data=extract_file('deliveries.csv')
    extra_runs_data=id_wise_data(matches_of_2016,deliveries_data)
    
    #print(extra_runs_data)

    return extra_runs_data 

def plot_of_extra_runs_given_per_team_in_2016(plot_data):
    x=plot_data.keys()
    y=plot_data.values()
    plt.bar(x,y)
    plt.title('Extra Runs Per Team In 2016')
    plt.xlabel('Teams')
    plt.ylabel('Extra Runs')
    plt.setp(plt.gca().get_xticklabels(),rotation=30,horizontalalignment='right')
    plt.show()



