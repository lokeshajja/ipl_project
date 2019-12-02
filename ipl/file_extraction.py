import os
import sys
import csv





    
def extract_matches_data(file_name):
    
    file=open('matches.csv','r')
    raw_data=csv.DictReader(file)
    data_array=list(raw_data) 


    return data_array





def extract_deliveries_data(file_name):

    file=open('deliveries.csv', 'r')
    delivery_data=csv.DictReader(file)
    delivery_stats=list(delivery_data)


    return delivery_stats






def  extract_file(file_name):

    if file_name=='matches.csv':
        matches_data=extract_matches_data(file_name)
        extracted_file_data=matches_data
    elif file_name=='deliveries.csv':
        deliveries_data=extract_deliveries_data(file_name)   
        extracted_file_data=deliveries_data
    else:
        pass
        

    return extracted_file_data
    