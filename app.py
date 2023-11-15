from flask import Flask, request, render_template


from stories import *

app = Flask(__name__)

@app.route('/')
def show_home():
