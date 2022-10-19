import csv
import pandas 
from re import template
# with open('./UDEMY/day-25/weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for loop, row in enumerate(data):
#         if loop>0:
#             temperature.append(int(row[1]))
#     print(temperature)


# data = pandas.read_csv('./UDEMY/day-25/weather_data.csv')
# # print(sum(data['temp'])/len(data))

# # print(data[data.day=='Monday'])
# monday = data[data.day == "Monday"]
# print(monday.condition)

data = pandas.read_csv('./day-25/park.csv')
grey_squirrels = data[data['Primary Fur Color'] == "Gray"]
print(grey_squirrels)