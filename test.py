import csv
import chicago_bikeshare_helper as helper

with open("chicago.csv", "r") as file_read:
    data_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(file_read, skipinitialspace=True)]

column_list = helper.column_to_list(data_list, "Gender")
types, counts = helper.count_items(column_list)
print(sum(counts))