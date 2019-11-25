from matches_played_per_year import compute_and_plot_matches_played_per_year
from file_extraction import extract_file
from number_of_matches_won_by_each import matches_won_by_each
import os
import sys
import numpy as np



def main():
    #matches=extract_file('matches.csv')
    #print(matches[635][10])
    deliveries_data=extract_file('deliveries.csv')
    #compute_and_plot_matches_played_per_year(matches)
    #win_data=matches_won_by_each(matches)
    #print(win_data)
    #plot_the_data(win_data)
    print(deliveries_data[12346])

    
if __name__=="__main__":
    main()