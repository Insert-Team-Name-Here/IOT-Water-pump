from flask import Flask
from gpiozero import LED
import time
#these are importing modules required for this project

relay = LED(14)
relay2 = LED(15)
#assigning the relays an LED

app = Flask(__name__)
#assigning Flask a variable name so that it is easier to run code with it in later on

@app.route('/',methods=['GET'])
#doing a GET on the web page

"""this function will return what is displayed on the main page"""
def index():
    return 'Main page'

@app.route('/on')
#turning on the relays through the function below

"""turning on the relays and printing hi to check the function is working properly"""
def on():
    print("hi")
    relay.on()
    relay2.off()
    return 'on'

@app.route('/off')
#shutting off the relays through the function below
"""turning off the relays and printing hi to check the function is working properly"""
def off():
    print("hi")
    relay.off()
    relay2.on()
    return 'off'

@app.route('/go')
#running the function go

"""this function turns on the relays so it sprays water"""
def go():
    relay.on()
    relay2.off()
    time.sleep(3)
    relay.off()
    relay2.on()
    return ('go')

"""accessing the web page through the relevant port (8000 is usually home) and host"""
if __name__ == '__main__':
    app.run(debug=True, port = 8000 , host='0.0.0.0')
