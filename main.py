import logging
import numpy as np 
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! CI'

@app.route('/newname/<name>')
def newroute(name):
    """parameter"""
    return "My name is {}".format(name)


@app.route('/location/<country>/<town>')
def location(country = None, town = None):
    """parameter"""
    return "I am located in : {}, {}".format(country,town)

@app.route('/bmi/<weight_in_kg>/<height_in_cm>')
def bmi(weight_in_kg = None, height_in_cm = None):
    """parameter"""

    bmi_index = np.round(int(weight_in_kg)/(int(height_in_cm)/100)**2,2)
    if bmi_index <= 18:
        status = 'Oh, no ... It seems that you are underweight'
    elif 18 < bmi_index <=22:
        status = 'Don\'t worry, that\'s Normal!'
    elif 22 < bmi_index <= 25:
        status = 'Status: Overweight'
    else: 
        status = 'Status: Obese'

    return "Your BMI is {}. -- > {}".format(bmi_index, status)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)