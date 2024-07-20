# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# # print(data)
# #
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #    data = csv.reader(data_file)
# #    temperatures = []
# #    for row in data:
# #        temperatures.append(row[1])
# # temperatures.remove("temp")
# # temperatures = [int(temp) for temp in temperatures]
# # print(temperatures)



# import pandas
# Once you've read the CSV your now have a dataframe that you saved into "data" variable below.
# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # |data| is the Dataframe (Entire table/csv) - is an Object
# print(type(data["temp"])) # |data["temp"]| is the Series (Column) - is an Object

# data_dict = data.to_dict()
# print(data_dict)"

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

 # Get data in Columns
# print(DATAFRAME[SERIES]
# print(data["condition"])
# print(data.condition)

 # To understand get data in rows
# print(data)

 # Get data in Rows
#  1. Call dataframe
#  2. Call series name
#  3. Call a value from the row/rows being examined. | Will find row that has the value your seeking.
# print(DATAFRAME[SERIES == ROW]
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.temp == 14])
# This is filtering the columns by rows.

# Monday's info
# monday = data[data.day == "Monday"]

# Getting Monday's specific temperature
# print(type(monday.temp))
# print(monday.temp)
# print(type(monday.temp[0]))
# print(monday.temp[0])

# celsius = monday.temp[0]
# fahrenheit = (celsius * 9/5) + 32
# print(fahrenheit)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Michael"],
#     "scores": [76, 70, 92],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Squirrel Project
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231226.csv")
data_for_fur_color = (squirrel_data["Primary Fur Color"].value_counts())
print(data_for_fur_color)
data_for_fur_color.to_csv("squirrel_counts")