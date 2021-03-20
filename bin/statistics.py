#Returns a tuple of 2 array, the first is the ages and the second is the corresponding percentage chance of death.
#Example: ([1,2,3], [0.1, 0.3333, 0.23])
def deathpercentagebyage(rows):
    ages = []
    count = []
    deathcount = []
    for row in rows:
        if row[0] in ages:
            count[ages.index(row[0])] += 1
            if row[2] == 1:
                deathcount[ages.index(row[0])] += 1
        else:
            ages.append(row[0])
            count.append(0)
            deathcount.append(0)
    deathpercentage = []
    for i in range(len(count)):
        if count[i] == 0:
            deathpercentage.append(0)
        else:
            deathpercentage.append(deathcount[i]/count[i])
    return (ages, deathpercentage)

#Returns the time difference between date confirmed and date onset in days.
def timedelta(rows):
    timedeltaArr = []
    for row in rows:
        timedeltaArr.append((row[4] - row[3]).total_seconds() /86400)
    return timedeltaArr

