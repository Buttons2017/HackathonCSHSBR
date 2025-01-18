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
fridge = 0.0
laundry=0.0
dryer=0.0
centerAC = 0.0
windowCount = 0.0
windowTime = 0.0
windowCost = 0.0
shower = 0.0
sink = 0.0
toilet = 0.0
totalKWH = 0.0
totalGallons = 0.0
totalWaterCost = 0.0

# Define routes

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter, lightCount, lightHours, kWHlights, dishwasher, tv, oven, fridge, dryer, laundry, centerAC, \
        windowCount, windowTime, windowCost, shower, sink, toilet, totalKWH, totalKWHC, totalGallons, totalWaterCost
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
        elif 'fridge' in request.form:
            fridge = round(0.05*24 * float(request.form.get('fridge', '')), 1)
        elif 'laundry' in request.form:
            laundry = round(1.5/7 * float(request.form.get('laundry', '')), 1)
        elif 'dryer' in request.form:
            dryer = round(4.5/7 * float(request.form.get('dryer', '')), 1)
        elif 'centerAC' in request.form:
            centerAC = round(3.5*float(request.form.get('centerAC', '')))
        elif 'windowCount' in request.form:
            windowCount = int(request.form.get('windowCount', ''))
            windowTime = float(request.form.get('windowHours', ''))
            windowCost = round(windowCount * windowTime * 0.618,1)
        elif 'shower' in request.form:
            shower = round((150/60)*int(request.form.get('shower')),1)
        elif 'sink' in request.form:
            sink = round((200/60)*int(request.form.get('sink')),1)
        elif 'toilet' in request.form:
            toilet = round(0.47*int(request.form.get('toilet')),1)

        totalKWH = round(kWHlights+dishwasher+tv+oven+fridge+laundry+dryer+centerAC+windowCost+shower+sink+toilet,1)
        totalKWHC = round(totalKWH*0.17,2)

        totalGallons = round(shower+sink+toilet,1)
        totalWaterCost = round(totalGallons*(5/750),2)

    return render_template('index2.html', counter=counter, lightCount=lightCount, lightHours=lightHours,
                           kWHlights=kWHlights, dishwasher=dishwasher, tv=tv, oven=oven, fridge=fridge, laundry=laundry,
                           dryer=dryer, centerAC=centerAC, windowCost=windowCost, shower=shower, sink=sink, toilet=toilet,
                           totalKWH=totalKWH, totalKWHC=totalKWHC, totalGallons=totalGallons, totalWaterCost=totalWaterCost)


@app.route('/test')
def test():
    return "Goodbye, cruel world..."

@app.route('/main')
def stub():
    return render_template("index.html")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)