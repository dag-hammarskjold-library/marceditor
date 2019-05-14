from flask import Flask, Response, abort, jsonify, render_template, request, url_for
from .config import DevelopmentConfig

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('index.html'))