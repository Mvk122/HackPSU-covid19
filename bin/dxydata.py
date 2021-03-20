"""
Data ingest form for dxydata.csv
Returns a python array with the format:
[
    [AGE(int), GENDER(boolean), OUTCOME(integer), DATE_ONSET(datetime), DATE_CONFIRMED(datetime)]
]
Gender returns True if male, false if female 
outcome returns 0 if recovered, 1 if the patient died.
"""
import csv 

def get_data_array(filename):
    with open(filename, "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            print(row[7])

def validaterow(row):
    pass
            
