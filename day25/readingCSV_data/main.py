# Reading CSV data with Python

# import csv
#
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Pandas is a library that is used for data analysis.
# Used for data manipulation, analysis and cleaning.
# http://pandas.pydata.org/

import pandas

data = pandas.read_csv('weather_data.csv')

# # To get a column from the data frame
# data_dict = data.to_dict()
# print(data_dict)
#
# # To Series - Convert a column to a series
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # Get the average of the list of temperatures
# print(data['temp'].mean())
#
# # Get the maximum temperature in the list
# print(data['temp'].max())
#
# # Get the data in a column another way
# print(data.condition)

# Get the data in a row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
# print(monday.condition)

# Convert the temperature from Fahrenheit to Celsius
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')

