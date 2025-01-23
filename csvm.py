import csv

with open("D:\python\weather.csv") as file:
    data=list(csv.reader(file))
    print(data)

city=input("enter city name")
for row in data[1:]:
    if(city == row[0]):
        print(row[1])
    else:
        print("invalied city")
