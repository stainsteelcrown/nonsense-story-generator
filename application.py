import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def story_generation():    
    a = ['This is the beginning of the story']

    for i in range(0, 3):
        return a[i]
        nextLine = raw_input()
        a.append(nextLine)
        os.system('clear')

    return "\n".join(a)
    
if __name__ == '__main__':
    app.run()
