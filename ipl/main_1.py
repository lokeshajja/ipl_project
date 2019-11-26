from matches_played_per_year import compute_and_plot_matches_played_per_year
from file_extraction import extract_file
from number_of_matches_won_by_each import matches_won_by_each
#from plot_win_data import plot_the_winning_data
import os
import sys
import numpy as np



def main():
    matches=extract_file('matches.csv')
    compute_and_plot_matches_played_per_year(matches)
    #deliveries_data=extract_file('deliveries.csv')
    #1st task of ipl project
    #plot_the_winning_data(win_data)
    #2nd task of ipl project

    
if __name__=="__main__":
    main()