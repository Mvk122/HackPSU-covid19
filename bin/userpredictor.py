from sklearn.preprocessing import PolynomialFeatures
import numpy as np

def normalise(x, modifier):
    return (x/(x+modifier))

def get_death_chance(age, gender, days_since_onset, deathbyagemodel, agemodel_rmse_and_degree,  deathbydelaymodel, delaymodel_rmse_and_degree, maledeathchance, femaledeathchance):
    agedeathscore = deathbyagemodel.predict(PolynomialFeatures(degree=agemodel_rmse_and_degree[0], include_bias=False).fit_transform(np.array([age]).reshape((-1,1))))
    delaydeathscore = deathbydelaymodel.predict(PolynomialFeatures(degree=delaymodel_rmse_and_degree[0], include_bias=False).fit_transform(np.array([days_since_onset]).reshape((-1,1))))

    #Gender resolves to True if male
    if gender:
        genderweight = normalise(maledeathchance, 2)
    else:
        genderweight = normalise(femaledeathchance, 2)
    delayweight = 2* normalise(delaydeathscore[0], 0.1)
    print(delaydeathscore, delayweight)
    ageweigth  = 3* normalise(agedeathscore[0], 0.01)

    return (genderweight + delayweight + ageweigth) *(2)
