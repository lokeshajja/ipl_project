import csv


def extract_file_data(file_name):

    file = open(file_name, 'r')
    raw_data = csv.DictReader(file)
    data_array = list(raw_data)

    return data_array
