'''
1. open csv file and convert to extractable data format 
2. extract the year and number of matches played data
3. plot the graph with suitable representation
'''
import os
import sys
import numpy as np
from matplotlib import pyplot as plt

os.system('cls')


def organized_data(f):
    
    raw_data=f.read()
    organised_data1=list(((raw_data.rstrip()).split('\n')))
    #print(organised_data)
    organised_data=[]
    for data in organised_data1:
        id_wise_data=tuple(list(data.rstrip().split(',')))
        organised_data.append(id_wise_data[:-1])
        data_array=np.array(organised_data)


    return data_array
    
f=open('matches.csv', 'r')
data_array1=organized_data(f)

def years_of_matches(data_array1):
    years=[]
    for i in data_array1[1:]:
        year=i[1]
        if year not in years:
            years.append(year)
    years.sort()
    return years


seasons=years_of_matches(data_array1)
# returns seasons print(seasons)

def matches_year_wise(seasons,data_array1):
    matches_per_year={}
    for s in seasons:
        matches_per_year[s]=0
    #print(matches_per_year)


    for dats in data_array1[1:]:
        #print(dats[1])
        if dats[1] in matches_per_year:
            matches_per_year[dats[1]]+=1

    return matches_per_year






plot_data=matches_year_wise(seasons,data_array1)
#print(plot_data)
    

def plotting_data(plot_data):
    #print(plot_data)
    years=list(plot_data.keys())
    matches=list(plot_data.values())
    

    plt.bar(years,matches)
    plt.show()





plotting_data(plot_data)






