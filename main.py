from flask import Flask, request
import pandas as pd

df = pd.read_csv('./data/diagnoses2019-2.csv')
df.columns

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return 'this is an API service for MN diagnosis description details'

@app.route('/preview', methods=["GET"])    
def preview():
    top10rows = df.head(10)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/diag/<value>', methods=["GET"])    
def diagdes(value):
    #Psoriasis
    print('value: ', value)
    filtered = df[df['diagnosis_description'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else:
        return filtered.to_json(orient="records")

@app.route('/diag/<value>/sex/<value2>')    
def diagdes2(value, value2):
    filtered = df[df['diagnosis_description'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else:
        return filtered2.to_json(orient="records")

if __name__ == '__main__':
    app.run(debug=True)