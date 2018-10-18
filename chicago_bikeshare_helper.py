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

def count_user_type(data_list):
    user_type_list = column_to_list(data_list, "User Type")
    user_type_counts_dict = {}
    for user_type in user_type_list:
        if user_type not in user_type_counts_dict:
            user_type_counts_dict[user_type] = 1
        else:
            user_type_counts_dict[user_type] += 1
    
    user_type_counts = []
    for i in user_type_counts_dict.keys():
        user_type_counts.append(user_type_counts_dict[i])

    return user_type_counts

def get_user_types(data_list):
    user_type_list = set(column_to_list(data_list, "User Type"))
    return user_type_list