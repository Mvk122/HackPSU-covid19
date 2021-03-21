# COVID 19 Risk Assesment

Using Polynomial Regression Machine Learning algorithms, the covid 19 assesment tool can calculate a user's covid 19 risk to help hospitals prioritise limited hospital resources to those that need them the most.

## [Try it out!](https://mun-online.herokuapp.com/)

## [Project Video Explanation](https://www.youtube.com/watch?v=GaMl2lgCVcc)

## [Project Devpost](https://devpost.com/software/covid-19-risk-assesment-k0xcm6)

## Built with

* scikit-learn for creating the Prediction Model.
* Flask for the website deployment.
* MySQL for the database backend.

## Try it out locally

* Run `pip install -r requirements.txt`
* Run `python website.py`
* Connect to `localhost:5000` on your web browser and try the website!

## Inspiration
The project was inspired by the world's initiative to flatten the curve for covid19 in the global pandemic to ensure that critical risk patients receive the care that they require. The effect that covid 19 can have on a person is highly dependant on how quickly they get medical care as soon as symptoms are onset as well as their age and gender. Thus we created a risk calculator to prioritise patients based on their needs.
## What it does

The app uses machine learning based on thousands of previous covid cases to asses the risk for an individual based on their:
* Gender 
* Age
* Time since they first exhibited symptoms.

The app then gives the user a score out of 10 based on the above factors to gauge their risk of death from covid 19. It does so by using machine learning to create a model that can then be extrapolated from to gauge an individual's risk based on these 3 key factors. 

The machine learning algorithm uses a polynomial regression algorithm to create a model for each of the 3 factors, normalises the user's score for each factor and then displays the risk to the user out of 10

## How we built it

We searched the internet for useful covid 19 patient data which was quite hard to find due to patient confidentiality laws. We then formatted the data that we found into csv files that would be read into the program. Once the data was read into the program, we used the following to parse the data:

### numpy 
Numpy was used to transform the data arrays into a format that can be used by the polynomial regression algorithm 

### scikit-learn

Scikit-learn was a simple to use machine learning library that was used to create the models. We used a polynomial regression algorithm to model the effects of: 

1. Age
2. Days since symptoms appearing and going to the hospital

As for the effect of gender, we could just take an average based on the chance that a patient who died was male or female so no machine learning was required for this aspect.

## Challenges we ran into

### normalising the data 
For large values, especially in the days since onset, the machine learning algorithm would spit out astronomically large or small numbers, in the order of 10^-40 to 10^60. To normalise this and get a score out of 10, we devised a quick and easy normalisation function, 
### x/(x+margin)

For all positive values, this function would return a value between 0 and 1, the margin can be any positive number to change how sensitive the value is. We used this formula as its function has a horizontal asymptote at y=1

### Finding a proper degree for the polynomial 

Being new to the world of machine learning, we realised that we didn't know the proper "degree" to which our machine learning algorithm should be tuned to, the degree referring to the maximum exponent of the polynomial, eg a third degree polynomial would be of the form ax^3 + bx^2 + cx + d. 

We found out that a statistic that can be used to find out how well a model fits the data is the root mean square error between a predicted value and a real value. We used this to our advantage by running through each degree from 1 through 15, creating a model with that degree and then with our table of values we calculated the rmse for each model. We then used the model with the lowest rmse for the final model. the code for this algorithm is as such: 

```python
def getBestPolynomialFit(x,y, max_degree):
    degreearray = []
    npY = np.array(y)
    npX = np.array(x).reshape((-1,1))
    for i in range(1, max_degree):
        predictions = createPolynomialRegression(x,y,i).predict(PolynomialFeatures(degree=i, include_bias=False).fit_transform(npX))
        degreearray.append([i, rmse(predictions, npY)])

    #Lowest rmse is [degree (int), rmse score (float)]
    lowest_rmse = degreearray[0]
    for degree in degreearray:
        if degree[1] < lowest_rmse[1]:
            lowest_rmse = degree
    
    return (lowest_rmse)
```

Could this lead to overfitting? possibly. But we didn't know any better and we had the afforementioned normalisation function to ensure values returned were normal anyway.Furthermore we checked that the values were sensible by plotting the continous outputs of each function with `matplotlib`

## Accomplishments that we're proud of

We're quite proud to be creating such an extensive program especially one that uses machine learning in our first hackathon, especially since prior to this event we didn't know each other. Furthermore most of what we did in this project was learnt while we did the project which is quite an accomplishment in 48 hours.


## What we learned

* Learnt what polynomial regression algorithms are.
* Learnt to use machine learning algorithms and how to fit models with the right data.
* Using mathematics to normalise the data.
* Using Flask. 
* Using HTML and CSS.
* Using Heroku to deploy the app.

## What's next for COVID 19 Risk Assesment

Our future plans include adding more information on the website to explain to users what their score means and educating users on the main factors that contribute to covid 19 risk. Even if this is an application to be used more by hospitals since anyone who feels they might have covid should be going to the hospital anyway; it provides users with a proper learning tool as to the risk factors of covid. 

Furthermore we would like to polish our machine learning algorithms and get more data to further improve our application. 

## Created By 
* Madhav Khandhar
* Jay (Zhengjie) Zhou
* AounTech( Ali Aoun)
