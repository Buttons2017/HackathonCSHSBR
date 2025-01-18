import os

from flask import Flask
import math
from flask import Blueprint, render_template, request

# Create the Flask app
app = Flask(__name__)



# Initialize counter and text
counter = 0
submitted_text = ""
lightCount = 0
lightHours = 0
kWHlights = 0.0
dishwasher = 0.0
tv = 0.0
oven = 0.0

# Define routes

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter, lightCount, lightHours, kWHlights, dishwasher, tv, oven
    if request.method == 'POST':
        # Check which form was submitted
        if 'increment_button' in request.form:
            counter += 1  # Handle counter increment
        elif 'lightCount' in request.form:
            lightCount = request.form.get('lightCount', '')
            lightHours = request.form.get('lightHours', '')
            kWHlights = round((int(lightCount) * int(lightHours) * .06),2)
        elif 'dishwasher' in request.form:
            dishwasher = float(request.form.get('dishwasher', ''))
        elif 'tv' in request.form:
            tv = round(0.05*float(request.form.get('tv', '')),1)
        elif 'oven' in request.form:
            oven = round(4*float(request.form.get('oven', '')),1)

    return render_template('index2.html', counter=counter, lightCount=lightCount, lightHours=lightHours,
                           kWHlights=kWHlights, dishwasher=dishwasher, tv=tv, oven=oven)


@app.route('/test')
def test():
    return "Goodbye, cruel world..."

@app.route('/main')
def stub():
    return render_template("index.html")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)