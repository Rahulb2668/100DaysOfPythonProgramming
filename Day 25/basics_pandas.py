# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

import pandas

data = pandas.read_csv("./weather_data.csv")

# Getting the column from the data frame
# print(data["temp"])

# Getting single row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Getting a values and applying operations

monday_temp = data[data.day =="Monday"].temp
monday_temp_F = monday_temp * 9/5 + 32
print(f"Monday Temp in Fahrenheit {monday_temp_F[0]}")