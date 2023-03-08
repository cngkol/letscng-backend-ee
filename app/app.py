from flask import Flask, request, jsonify
import sqlite3
import traceback
import pandas as pd
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/getRiders')
def get_riders():
    phone = request.args.get('phone')
    if phone==None:
        sqliteConnection = sqlite3.connect('../ee_db.sqlite3')
        print("DB init")
        query = 'select * from participants;'
        df = pd.read_sql_query(query, sqliteConnection)
        return df.to_json(),"200"
    else:
        sqliteConnection = sqlite3.connect('../ee_db.sqlite3')
        q = "SELECT * FROM participants WHERE contact = " + phone + ";"        
        df = pd.read_sql_query(q, sqliteConnection)
        return df.to_json(), "200"


@app.route('/addRider')
def add_rider():
    sqliteConnection = sqlite3.connect('../ee_db.sqlite3')
    cursor = sqliteConnection.cursor()
    rider_str = request.args.get('data')
    rider_str = unquote(rider_str)
    print(rider_str)

    try:
        dat = rider_str.split("|")
        q = 'INSERT INTO participants VALUES (' + str(dat)[1:-1] + ')'
        cursor.execute(q)
        sqliteConnection.commit()
        sqliteConnection.close()
        return "200"
    except Exception as ex:
        return jsonify(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))), "500"



@app.route('/setRiderDuration')
def set_duration():
    sqliteConnection = sqlite3.connect('../ee_db.sqlite3')
    cursor = sqliteConnection.cursor()
    dur = request.args.get('dur')
    phone = request.args.get('phone')

    try:
        q = "UPDATE participants SET duration=" + dur + " WHERE contact=" + phone + ";"
        cursor.execute(q)
        sqliteConnection.commit()
        q = "SELECT * FROM participants WHERE contact = " + phone + ";"
        df = pd.read_sql_query(q, sqliteConnection)
        sqliteConnection.close()
        return df.to_json(), "200"

    except Exception as ex:
        return jsonify(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))), "500"


@app.route('/setRiderBike')
def set_bike():
    sqliteConnection = sqlite3.connect('../ee_db.sqlite3')
    cursor = sqliteConnection.cursor()
    bike_type = request.args.get('bike')
    phone = request.args.get('phone')

    try:
        q = "UPDATE participants SET bike_type=" + bike_type + " WHERE contact=" + phone + ";"
        cursor.execute(q)
        sqliteConnection.commit()
        q = "SELECT * FROM participants WHERE contact = " + phone + ";"
        df = pd.read_sql_query(q, sqliteConnection)
        sqliteConnection.close()
        return df.to_json(), "200"

    except Exception as ex:
        return jsonify(''.join(traceback.format_exception(etype=type(ex), value=ex, tb=ex.__traceback__))), "500"


# main driver function
if __name__ == '__main__':
    app.run()