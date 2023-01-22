from flask import Flask, render_template, request


app= Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/calcaguras')
def calcaguras():
    return render_template('calcaguras.html')