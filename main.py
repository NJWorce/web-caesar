from flask import Flask, request, redirect, render_template
import cgi
import os
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    return render_template('caesar-form.html')

@app.route('/', methods = ['POST'])

def encrypt():
    rotated_string=''
    rot = request.form['rot']
    text = request.form['text']

    rot = int(rot)

    rotated_string = rotate_string(text, rot)

    return render_template('caesar-form.html', rotated_string=rotated_string)
app.run()
