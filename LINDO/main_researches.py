#!/usr/bin/python


# install flask:
# pip install --user flask
# run app with command:
# FLASK_APP=start.py flask run
# navigate to
# http://127.0.0.1:5000/calculate?first=2&second=5
# everything after ? optional
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/calculate", methods=['GET'])
def calculate():
    import prepareDataLINDO
    import research2
    import research2_1
    import research2_2
    import research2_3
    import research2_4
    import research2_5
    import research3_1_1
    import research3_1_2
    import research3_1_3
    import research3_2_1
    import research3_2_2
    import research3_2_3
    import research3_3_1
    import research3_3_2
    import research3_3_3
    import research4_1
    import research4_2
    import research4_3
    import research5_1_1
    import research5_1_2
    import research5_1_3
    import research5_2_1
    import research5_2_2
    import research5_2_3
    import research6
    import research6_1
    import research6_2
    import research6_3
