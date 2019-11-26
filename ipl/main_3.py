from extras_of_year_2016 import plotting_data
from extras_of_year_2016 import plot_of_extra_runs_given_per_team_in_2016
import os
import sys
import numpy as np


def main():
    plot_data=plotting_data()
    plot_of_extra_runs_given_per_team_in_2016(plot_data)
    #print(plot_data)


if __name__=="__main__":
    main()
    
    









