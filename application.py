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

#What I am trying to do here is take the original python program that
#worked in console and make it work with Flask.  
@app.route('/')
def story_generation():    

#Initializing my basic form or persistance which is a list
    a = ['This is the beginning of the story']

#The range can be changed to make a longer story but this
#code only works in the interpreter.  I need to update it 
#to work with Flask and make this a web application but
#the logic is there
    for i in range(0, 3):
        return a[i]
        nextLine = raw_input()
        a.append(nextLine)
        os.system('clear')

    return "\n".join(a)
    
#Ensuring the script does not run from an imported module
#And enabling debugging which must be disabled on a production
#server and can be commented out.
if __name__ == '__main__':
    app.debug = True
    app.run()
