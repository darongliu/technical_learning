import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    print('run:', time.time())
    return {'time': time.time()}