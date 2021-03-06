
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt
import chicago_bikeshare_helper as helper

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    data_list = [{key: value for key, value in row.items()}
        for row in csv.DictReader(file_read, skipinitialspace=True)]
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

helper.print_data_list(data_list, 0, 20)

input("\nPress Enter to continue...")
# TASK 2
# Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

helper.print_data_list_gender(data_list, 0, 20)

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# Create a function to add the columns(features) of a list in another list in the same order
gender_list = helper.column_to_list(data_list, "Gender")

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(gender_list[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(gender_list) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(gender_list) == 1551505, "TASK 3: Wrong lenght returned."
assert gender_list[0] == "" and gender_list[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# Count each gender. You should not use a function to do that.
male = len([gender for gender in gender_list if gender == "Male"])
female = len([gender for gender in gender_list if gender == "Female"])


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
count_gender = helper.count_gender(data_list)


print("\nTASK 5: Printing result of count_gender")
print(count_gender)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender) == 2, "TASK 5: Wrong lenght returned."
assert count_gender[0] == 935854 and count_gender[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
most_popular_gender_answer = helper.most_popular_gender(data_list)


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender_answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender_answer) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender_answer == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = helper.column_to_list(data_list, "Gender")
types = ["Male", "Female"]
quantity = helper.count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

user_type_list = helper.column_to_list(data_list, "User Type")
types = helper.get_user_types(data_list)
quantity = helper.count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User type')
plt.xticks(y_pos, types)
plt.title('Quantity by User Type')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# Answer the following question
male, female = helper.count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = input("Type your answer here.\n")
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = helper.column_to_list_sorted_int(data_list, "Trip Duration")
min_trip = trip_duration_list[0]
max_trip = trip_duration_list[-1]
mean_trip = helper.calculate_mean(trip_duration_list)
median_trip = helper.calculate_median(trip_duration_list)


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# Check types how many start_stations do we have using set()
user_types = set(helper.column_to_list(data_list, "Start Station"))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
#      """
#      Example function with annotations.
#      Args:
#          param1: The first parameter.
#          param2: The second parameter.
#      Returns:
#          List of X values
#
#      """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
answer = input("Will you face it?\n")

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = helper.column_to_list(data_list, "Gender")
    types, counts = helper.count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------