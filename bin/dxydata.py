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
import string
from datetime import datetime

def get_data_array(filename):
    with open(filename, "r", encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        validatedrows = []
        formattedrows = []
        for row in csv_reader:
            if validaterow(row):
                validatedrows.append(row)
        for row in validatedrows:
            formattedrows.append(formatrow(row))
    return formattedrows



#Returns a tuple of (date_onset and date_confirmed)
def getDates(row):
    symptom_onset_present = True
    hospital_visit_present = True
    try:
        symptomtime = datetime.strptime(row[8], "%m/%d/%Y")
    except:
        symptom_onset_present = False
    try:
        hospitaltime = datetime.strptime(row[10], "%m/%d/%Y")
    except:
        hospital_visit_present = False
    
    if symptom_onset_present:
        if hospital_visit_present:
            return (symptomtime, hospitaltime)
        else:
            return (symptomtime, symptomtime)
    elif hospital_visit_present:
        return (hospitaltime, hospitaltime)
    else:
        return (datetime(2023, 1 ,1), datetime(2023,1,1))


def formatrow(row):
    dates = getDates(row)
    return [
        int(row[7]),
        True if row[6] == "male" else False,
        1 if row[18] == "1" else 0,
        dates[0],
        dates[1]        
    ]


def validaterow(row):
    def isNum(entry):
        for digit in entry:
            if digit not in string.digits:
                return False
        return True
 
    def isGender(entry):
        return (entry=="male" or entry=="female")

    def notBlank(entry):
        return (entry !="")

    validators = [
        isNum(row[7]),
        notBlank(row[7]),
        isGender(row[6]),
        notBlank(row[18]),
        (notBlank(row[8]) or notBlank(row[10]))
    ]

    for validator in validators:
        if not validator:
            return False
    return True
