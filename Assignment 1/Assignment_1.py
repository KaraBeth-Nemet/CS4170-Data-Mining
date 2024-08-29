import csv
with open('mutations.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  individual_sample_number = 0
  
  for lines in csvFile:
    individual_sample_number += 1

print("The number of individual samples in the file is: ", individual_sample_number)
