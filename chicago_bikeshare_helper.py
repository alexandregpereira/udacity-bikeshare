def print_data_list(data_list, start_index, stop_index):
    for row in data_list[:stop_index]:
        print(row)

def print_data_list_gender(data_list, start_index, stop_index):
    for row in data_list[:stop_index]:
        gender = row['Gender']
        print(gender if gender else "Unknown")

def column_to_list(data, column_name):
    column_list = [data_row[column_name] for data_row in data]
    return column_list

def count_gender(data_list):
    gender_list = column_to_list(data_list, "Gender")
    male = len([gender for gender in gender_list if gender == "Male"])
    female = len([gender for gender in gender_list if gender == "Female"])
    return [male, female]

def most_popular_gender(data_list):
    count_gender_list = count_gender(data_list)
    return "Male" if count_gender_list[0] > count_gender_list[1] \
        else "Female" if count_gender_list[1] > count_gender_list[0] \
        else "Equal"