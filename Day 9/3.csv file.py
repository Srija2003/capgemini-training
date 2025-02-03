import csv

file = open("Day 9/numbers.csv", "w")  
writer = csv.writer(file)  
writer.writerow(["Num1", "Num2", "Num3"])  

num1 = input("Enter first number: ")  
num2 = input("Enter second number: ")  
num3 = input("Enter third number: ")  
writer.writerow([num1,num2,num3])  
file.close()  
print("Data saved to numbers.csv")  
