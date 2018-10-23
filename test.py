import csv
import chicago_bikeshare_helper as helper

with open("chicago.csv", "r") as file_read:
    data_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(file_read, skipinitialspace=True)]

user_types = set(helper.column_to_list(data_list, "Start Station"))
print(len(user_types))