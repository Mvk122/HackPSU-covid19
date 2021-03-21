from bin.readCSV import get_csv_array
from flask import Flask, render_template, request
from datetime import datetime
import traceback

from bin.dxydata import *
from bin.statistics import *
from bin.predictors import *
from bin.userpredictor import *

app = Flask(__name__)
rows = get_data_array('assets/dxydata.csv')
male, female = deathpercentagebygender(rows)
ages, agedeathpercentages = deathpercentagebyage(rows)
delays, delaydeathpercentages = deathpercentagebyhospitaldelay(rows)

age_rmse_and_degree = getBestPolynomialFit(ages, agedeathpercentages, 15)
agemodel = createPolynomialRegression(ages, agedeathpercentages, age_rmse_and_degree[0])

delay_rmse_and_degree = getBestPolynomialFit(delays, delaydeathpercentages, 15)
delaymodel = createPolynomialRegression(delays, delaydeathpercentages, 1)


@app.route('/')
def home_page():
    return render_template('Home.html')

@app.route('/evaluate/')
def evaluate():
    try:
        age = int(request.args.get('age'))
        gender = True if request.args.get('gender') == "male" else False
        onSetDelay = (datetime.today() - datetime.strptime(request.args.get('dateOnSet'), "%Y-%m-%d")).total_seconds() /86400
        
        deathchance = get_death_chance(age, gender, onSetDelay, agemodel, age_rmse_and_degree, delaymodel, [1,0.13], male, female)
        return render_template('ShowResult.html', chance=str(int(deathchance)))

    except Exception as e:
        traceback.print_exc()
        return "You did not input your information correctly"
    
if __name__ == "__main__":
    app.run(debug=True)