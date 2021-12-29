# -*- coding: utf-8 -*-

from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os

app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only


@app.errorhandler(Exception)
def server_error(err):
    return render_template('error.html'), 500

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        information = request.data
        print('received speed info is: ', information, '\n')
        
        return render_template('speedtest.html')
    else:
        return render_template('speedtest.html', download=0, upload=0,client="---")	



# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
