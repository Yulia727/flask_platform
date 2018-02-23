from flask import render_template
from flask_platform import app
from systeminfo import get_platform_info

info = get_platform_info()


@app.route('/')
def index():
    returnDict = {}
    returnDict['Greeting'] = 'How are you ?'
    returnDict['information'] = info
    return render_template("index.html",**returnDict)



