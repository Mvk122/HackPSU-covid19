from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def get_death_chance(age, gender, days_since_onset, deathbyagemodel, agemodel_rmse_and_degree,  deathbydelaymodel, delaymodel_rmse_and_degree, maledeathchance, femaledeathchance):
    agedeathscore = deathbyagemodel.predict(PolynomialFeatures(degree=agemodel_rmse_and_degree[0], include_bias=False).fit_transform(np.array([age]).reshape((-1,1))))
    delaydeathscore = deathbydelaymodel.predict(PolynomialFeatures(degree=delaymodel_rmse_and_degree[0], include_bias=False).fit_transform(np.array([days_since_onset]).reshape((-1,1))))

    #Gender resolves to True if male
    if gender:
        genderweight = 1 * maledeathchance
    else:
        genderweight = 1 * femaledeathchance
    delayweight = 1 * delaydeathscore[0]
    ageweigth  = 1 *agedeathscore[0]

    return (genderweight + delayweight + ageweigth) /3
