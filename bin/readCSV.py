"""
Data ingest form for outside-hubei-table.csv and latestdata.csv
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

def get_csv_array(filename):
    with open(filename, "r", encoding="utf8") as csv_file:
        # The super huge csv is separated by ; by mistake. cant afford to change.
        if "latestdata" in filename:
            csv_reader = csv.reader(csv_file, delimiter=";")
        else:
            csv_reader = csv.reader(csv_file, delimiter=",")
        validatedrows = []
        formattedrows = []
        for row in csv_reader:
            if validaterow(row):
                validatedrows.append(row)
        for row in validatedrows:
            formattedrows.append(formatrow(row))
    return formattedrows

def validaterow(row):
    if not row[0].isdigit():
        return False
    if not (row[1].lower() == "male" or row[1] == "female".lower()):
        return False
    return True

def getDates(row):
    symptom_onset_present = True
    hospital_visit_present = True
    try:
        symptomtime = datetime.strptime(row[2], "%d.%m.%Y")
    except:
        symptom_onset_present = False
    try:
        hospitaltime = datetime.strptime(row[3], "%d.%m.%Y")
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
        return (datetime(2023, 1, 1), datetime(2023, 1, 1))

def getOutCome(row):
    if row[4].lower() == "death":
        return 1
    return 0;

def formatrow(row):
    dates = getDates(row)
    return [
        int(row[0]),
        True if row[1].lower() == "male" else False,
        getOutCome(row),
        dates[0],
        dates[1]
    ]