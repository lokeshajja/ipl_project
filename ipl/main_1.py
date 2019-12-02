from matches_played_per_year import compute_and_plot_matches_played_per_year
from file_extraction import extract_file

import os
import sys
import numpy as np



def main():
    matches=extract_file('matches.csv')
    compute_and_plot_matches_played_per_year(matches)
    
   
    
if __name__=="__main__":
    main()