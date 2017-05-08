from flask import render_template, request, jsonify
from config import db, app
from models import *
import json


if __name__  ==	"__main__":
	app.run(debug=True, threaded=True, port= 3000)