import os
import sys
import numpy as np
from matplotlib import pyplot as plt




def plot_the_number_of_matches_per_year(matches_per_year):
    plot_data=matches_per_year
    years=list(plot_data.keys())
    matches=list(plot_data.values())
    plt.bar(years,matches)
    plt.show()

def compute_number_of_matches_yearwise1(matches):
    #print(matches)
    yr_ws_matches={}
    for match_1 in matches:
        if match_1['season'] not in yr_ws_matches:
            yr_ws_matches[match_1['season']]=1
        elif match_1['season']  in yr_ws_matches:
            yr_ws_matches[match_1['season']]+=1
        else:
            pass
    #print(yr_ws_matches)
    

    #print(yr_ws_matches)
    yr_ws_matches1={}
    for yr1 in sorted(yr_ws_matches.keys()):
        yr_ws_matches1[yr1]=yr_ws_matches[yr1]
    #print(yr_ws_matches1)


    return yr_ws_matches1



    

def compute_and_plot_matches_played_per_year(matches):
    matches_per_year=compute_number_of_matches_yearwise1(matches)
    plot_the_number_of_matches_per_year(matches_per_year)
    