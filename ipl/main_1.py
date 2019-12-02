from matches_played_per_year import compute_and_plot_matches_played_per_year
from number_of_matches_won_by_each import compute_and_plot_of_win_data
from extras_of_year_2016 import plotting_data
from extras_of_year_2016 import plot_of_extra_runs_given_per_team_in_2016
from most_econ_bowlers_2015 import compute_and_plot_most_economic_bowlers_of_2015
from max_centuries import compute_centuries_data_over_all_years
from file_extraction import extract_file
import os
import sys
import numpy as np





def main():


#plots number of matches played per year in all seasons    
    matches=extract_file('matches.csv')
    compute_and_plot_matches_played_per_year(matches)


#Plots a stacked bar chart of matches won of all teams over all the years of IPL.
    #compute_and_plot_of_win_data()


#For the year 2016 plot the extra runs conceded per team.
    #plot_data=plotting_data()
    #plot_of_extra_runs_given_per_team_in_2016(plot_data)


#For the year 2015 plot the top economical bowlers.
    #matches=extract_file('matches.csv')
    #deliveries_data=extract_file('deliveries.csv')
    #compute_and_plot_most_economic_bowlers_of_2015(matches,deliveries_data)


 #count the number of centuries scored in all the seasons of IPL   
    #compute_centuries_data_over_all_years()



    

if __name__=="__main__":
    main()