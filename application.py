#The MIT License (MIT)
#
#Copyright (c) 2014. Andrew Castano. Castano Engineering Company.
# 
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

#Importing the os so I can clear the terminal
import os

#Imported a Flask class and created an instance of the class
from flask import Flask
app = Flask(__name__)

from flask import render_template

#I am trying to figure out how to get the form data
from flask import request

# Default config values 
FLASK_DEBUG = 'false' if os.environ.get('FLASK_DEBUG') is None else os.environ.get('FLASK_DEBUG')

# Load config values specified above
application.config.from_envvar('APP_CONFIG', silent=True)

# Only enable Flask debugging if an env var is set to true
application.debug = application.config['FLASK_DEBUG'] in ['true', 'True']


#I am attempting to store information in the list Lines but it keeps
#getting overwritten everytime I post.
@app.route('/', methods=['GET', 'POST'])
def story_generation():    

#Initializing my basic form or persistance which is a list
    line = 'You are the first contributer and can start the first line'
    lines = []
    
    if request.method == 'POST':
        line = request.form['line'] 
        lines.append(line)

    return render_template('index.html', line = line, lines = lines)
    
#Ensuring the script does not run from an imported module
#And enabling debugging which must be disabled on a production
#server and can be commented out, eventually I will put this in a 
#configuration file.
if __name__ == '__main__':
    app.debug = True
    app.run()
