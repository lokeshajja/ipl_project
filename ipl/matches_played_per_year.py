import os
import sys
import numpy as np
from matplotlib import pyplot as plt



def compute_number_of_matches_yearwise(matches):
    data_array1=matches

    def years_of_matches(data_array1):
        years=[]
        for match in data_array1[1:]:
            year=match[1]
            if year not in years:
                years.append(year)
        years.sort()
        #print(years)
        return years



    def matches_year_wise(seasons,data_array1):
        matches_per_year={}
        for s in seasons:
            matches_per_year[s]=0
        #print(matches_per_year)


        for matches1 in data_array1[1:]:
            #print(matches[1])
            if matches1[1] in matches_per_year:
                matches_per_year[matches1[1]]+=1

        return matches_per_year
    



    seasons=years_of_matches(data_array1)
    # returns seasons print(seasons)
    plot_data=matches_year_wise(seasons,data_array1)
    

   
    return plot_data 

def plot_the_number_of_matches_per_year(matches_per_year):
    plot_data=matches_per_year
    years=list(plot_data.keys())
    matches=list(plot_data.values())
    

    plt.bar(years,matches)
    plt.show()



def compute_and_plot_matches_played_per_year(matches):
    matches_per_year=compute_number_of_matches_yearwise(matches)
    #print(matches_per_year)
    plot_the_number_of_matches_per_year(matches_per_year)
    