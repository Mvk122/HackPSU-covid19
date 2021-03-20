import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

#x and y are 1 dimensional python arrays
def createPolynomialRegression(x,y, degree):
    x = np.array(x).reshape((-1,1))
    y = np.array(y)
    x_ = PolynomialFeatures(degree=degree, include_bias=False).fit_transform(x)    

    model = LinearRegression().fit(x_,y)
    y_pred = model.predict(x_)
    return y_pred

def getBestPolynomialFit(x,y, max_degree):
    degreearray = []
    npY = np.array(y)
    for i in range(1, max_degree):
        predictions = createPolynomialRegression(x,y,i)
        degreearray.append([i, rmse(predictions, npY)])

    #Lowest rmse is [degree (int), rmse score (float)]
    lowest_rmse = degreearray[0]
    for degree in degreearray:
        if degree[1] < lowest_rmse[1]:
            lowest_rmse = degree
    
    return (lowest_rmse)





