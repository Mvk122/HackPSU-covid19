from bin.dxydata import *
from bin.statistics import *
from bin.predictors import *
from bin.userpredictor import *

import matplotlib.pyplot as plt
import time

rows = get_data_array('assets/dxydata.csv')
male, female = deathpercentagebygender(rows)
ages, agedeathpercentages = deathpercentagebyage(rows)
delays, delaydeathpercentages = deathpercentagebyhospitaldelay(rows)

age_rmse_and_degree = getBestPolynomialFit(ages, agedeathpercentages, 15)
agemodel = createPolynomialRegression(ages, agedeathpercentages, age_rmse_and_degree[0])

delay_rmse_and_degree = getBestPolynomialFit(delays, delaydeathpercentages, 15)
delaymodel = createPolynomialRegression(delays, delaydeathpercentages, delay_rmse_and_degree[0])

start_time = time.time()
deathchance = get_death_chance(49, True, 10, agemodel, age_rmse_and_degree, delaymodel, delay_rmse_and_degree, male, female)
print(time.time() - start_time)
print(deathchance)

"""
degree_and_rmse = getBestPolynomialFit(x,y, 12)

best_prediction = createPolynomialRegression(x,y, degree_and_rmse[0])

plt.bar(x, y, color="maroon", width=1)
plt.show()

agearr = np.array(ages).reshape((-1,1))
nagearr = PolynomialFeatures(degree=14, include_bias=False).fit_transform(agearr) 
y_pred = agemodel.predict(nagearr)
plt.bar(ages, y_pred, color="maroon", width=1)
plt.show()
"""