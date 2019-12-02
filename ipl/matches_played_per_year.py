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





def compute_number_of_matches_yearwise(matches):
   
    year_wise_match_counts={}
    for match in matches:
        year_wise_match_counts[match['season']] = year_wise_match_counts.get(match['season'],0)+1
    
    
    print(year_wise_match_counts)
    year_wise_matches={}
    for year in sorted(year_wise_match_counts.keys()):
        year_wise_matches[year]=year_wise_match_counts[year]


    return year_wise_matches





def compute_and_plot_matches_played_per_year(matches):

    matches_per_year=compute_number_of_matches_yearwise(matches)
    plot_the_number_of_matches_per_year(matches_per_year)
    