# Flask PY APP
from flask import Flask, jsonify,render_template
from flask_bootstrap import Bootstrap
 
import pandas as pd
 
#import pprint as pp

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/v1.0/Weatherpy/CsvFile/<CsvFile>")
def getDFtoHTML(CsvFile):
    # Read the csv file in
    return pd.read_csv(CsvFile).to_html
# base='assets\cities.csv'fl

def create_app():
    app=Flask(__name__)
    Bootstrap(app)
    return app

if __name__ =='__main':
    app.run(port=5000 debug=True)