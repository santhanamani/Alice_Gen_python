import glob
import io
import os
import uuid

import numpy as np
from flask import Flask, jsonify, make_response, render_template, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask_cors import CORS
# import RPi.GPIO as GPIO    # change

# GPIO.setmode(GPIO.BOARD)

app   = Flask(__name__)
CORS(app)

app.secret_key = "s3cr3t"
app.debug = False
app._static_folder = os.path.abspath("/")


# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   10 : {'name' : 'GPIO 10', 'state' : "GPIO.LOW"},   #change state value
   12 : {'name' : 'GPIO 12', 'state' : "GPIO.LOW"}
   }

# Set each pin as an output and make it low:


@app.route("/")
def main():
   pin = "RPi Web Server"
   # Pass the template data into the template main.html and return it to the user
   return render_template('index.html',  pin=pin)


@app.route("/datasend", methods=["POST"])
def datasend():
    jsdata = request.get_json(force=True)
    print(jsdata["id"])
    print(jsdata["name"])
    print(jsdata["state"])
    params = {"data": "success"}
    return jsonify(params)



# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      GPIO.output(changePin, GPIO.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      GPIO.output(changePin, GPIO.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)

   # Along with the pin dictionary, put the message into the template data dictionary:
   templateData = {
      'pins' : pins
   }

   return render_template('main.html', **templateData)


@app.route("/dataget", methods=["GET"])
def dataget():
   #params = {"data": "success"}
   # params = pins
   response = jsonify({"params":pins})
   response.headers.add("Access-Control-Allow-Origin" ,"*")
   return pins





if __name__ == "__main__":
   app.run(debug=True)
