import csv


def extract_data(file_name):

    with open(file_name, 'r') as file:
        raw_data = csv.DictReader(file)
        data_read = list(raw_data)

    return data_read
