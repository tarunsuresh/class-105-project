import csv
import math

with open("data.csv",newline='') as f :
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def Mean():
    n=len(data)
    totalSum=0
    for number in data:
        totalSum += int(number)
        print(int(number))
    print(totalSum)
    mean=totalSum/n
    return mean


square=[]

for number in data:
    dif=int(number)-Mean()
    squareItem=dif**2
    square.append(squareItem)

sum=0

for number in square:
    sum += int(number)

result=sum/(len(data)-1)

standardDeviation=math.sqrt(result)
print(standardDeviation)