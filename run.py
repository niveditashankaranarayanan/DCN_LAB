from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

#FOR TIME
@app.route('/time')
def current_time():
    present_time=datetime.now()
    time_now=present_time.strftime("%H :%M :%S")
    return time_now

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
