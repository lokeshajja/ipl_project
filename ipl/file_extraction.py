

import os
import sys
import numpy as np
from matplotlib import pyplot as plt



def  extract_file(file_name):
    
    def extract_matches_data(file_name):
        f=open('matches.csv','r')
        raw_data=f.read()
        organized_data1=list(((raw_data.rstrip()).split('\n')))
        organized_data=[]
        for data in organized_data1:
            id_wise_data=tuple(list(data.rstrip().split(',')))
            organized_data.append(id_wise_data[:-1])
            data_array=np.array(organized_data)    
        return data_array

    def extract_deliveries_data(file_name):
        f=open('deliveries.csv', 'r')
        delivery_data=f.read()
        delivery_data1=list(delivery_data.rstrip().split('\n'))
        #print(delivery_data1)

        delivery_stats=[]
        for delivery in delivery_data1:
            delivery_stat=list(delivery.split(','))
            delivery_stats.append(tuple(delivery_stat))

        #print(delivery_stats[115678])
        return delivery_stats


    if file_name=='matches.csv':
        matches_data=extract_matches_data(file_name)
        extracted_file_data=matches_data
    elif file_name=='deliveries.csv':
        deliveries_data=extract_deliveries_data(file_name)   
        extracted_file_data=deliveries_data
    else:
        pass

    return extracted_file_data
    