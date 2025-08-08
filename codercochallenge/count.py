import os
from flask import Flask #Imports the Flask class from the flask library.
import redis  #Imports the redis Python client so we can connect to a Redis database.

app = Flask(__name__) #Creates a Flask application object called app.
redis_host = os.getenv('REDIS_HOST', 'redis') #Gets the Redis host address from the environment variable REDIS_HOST, or uses 'redis' if that variable isn’t set.
redis_port = int(os.getenv('REDIS_PORT', 6379)) #Gets the Redis port number from the environment variable REDIS_PORT, or uses 6379 if that variable isn’t set, converting it to an integer
r = redis.Redis(host='redis', port=6379) #Creates a Redis connection object called r.

@app.route('/') #means when someone visits the root URL (/), run the welcome() function.
def welcome():
    return 'Welcome to the CoderCo Challenge'

@app.route('/count') #means when someone visits /count, run the count() function.
def count():
    count= r.incr('visits')
    return f'This site has been visted {count} times'

if __name__ == '__main__':  # The if statement checks: “Am I being run directly?”
        app.run(host='0.0.0.0', port = 5002) #If yes, it starts the Flask development server on port 5002.
