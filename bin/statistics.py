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


#Returns a tuple of 2 arrays the first is the delay and the second is the corresponding percentage chance
def deathpercentagebyhospitaldelay(rows):
    delays = []
    count = []
    deathcount = []
    for row in rows:
        if tdelta(row) in delays:
            count[delays.index(tdelta(row))] += 1
            if row[2] == 1:
                deathcount[delays.index(tdelta(row))] += 1
        else:
            delays.append(tdelta(row))
            count.append(0)
            deathcount.append(0)

    deathpercentage = []
    for i in range(len(count)):
        if count[i] == 0:
            deathpercentage.append(0)
        else:
            deathpercentage.append(deathcount[i]/count[i])
    return (delays, deathpercentage)


#Returns a tuple of maledeathpercentage, femaledeathpercentage
def deathpercentagebygender(rows):
    malecount = 0
    maledeathcount = 0
    femalecount = 0
    femaledeathcount = 0
    for row in rows:
        if row[1]:
            malecount += 1
            if row[2] == 1:
                maledeathcount += 1
        else:
            femalecount += 1
            if row[2] == 1:
                femaledeathcount += 1

    maledeathpercentage = maledeathcount / malecount
    femaledeathpercentage = femaledeathcount / femalecount
    return (maledeathpercentage, femaledeathpercentage)

def tdelta(row):
    return ((row[4] - row[3]).total_seconds() /86400)

#Returns the time difference between date confirmed and date onset in days.
def timedeltarray(rows):
    timedeltaArr = []
    for row in rows:
        timedeltaArr.append((row[4] - row[3]).total_seconds() /86400)
    return timedeltaArr

