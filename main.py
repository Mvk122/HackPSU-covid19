from bin.statistics import deathpercentagebyage, timedelta
from bin.dxydata import *
from statistics import *
from bin.predictors import *

import matplotlib.pyplot as plt

rows = get_data_array('assets/dxydata.csv')
x , y = deathpercentagebyage(rows)

degree_and_rmse = getBestPolynomialFit(x,y, 12)

best_prediction = createPolynomialRegression(x,y, degree_and_rmse[0])
print(degree_and_rmse)
plt.bar(x, best_prediction, color="maroon", width=1)
plt.show()
