from flask import Flask, render_template, request
from datetime import date

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def Check():
    leap=''
    if request.method == 'POST' and 'year' in request.form:
        leap = int(request.form['year'])
        if (leap % 4 == 0 and leap % 100 != 0) or (leap % 400 == 0):
            leap='a leap year'
        else:
            leap='not a leap year'
    return render_template("index.html",leap=leap)

app.run(host='0.0.0.0', port=8080)