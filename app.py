from flask import Flask, render_template, request
from math import hypot

app= Flask(__name__)

#starting route
@app.route('/')
def index():
    return render_template('base.html')

#this route loads the calculator layout
@app.route('/calcaguras')
def calcaguras():
    return render_template('calcaguras.html')

@app.route('/calculate', methods=['POST'])
def calculate():  #function that calculates the hypotenuse
    sideA= int(request.form['sideA']) #takes the value filled in the form referring to the side A
    sideB= int(request.form['sideB']) #takes the value filled in the form referring to the side B

    hypotenuseValueResult= round(hypot(sideA,sideB),2)#hypot calculates the hypotenuse and round rounds the decimal places

    return f"<h1 style='background-image: linear-gradient(to right, rgb(20, 147, 220), rgb(17, 54, 71));color:white;width: 100vw;height: 100vh;display: flex;flex-direction: row;justify-content: center;align-items: center;'>Hypotenuse Value= "+ str(hypotenuseValueResult)+ "</h1>"