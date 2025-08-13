import os
import random
from flask import Flask, render_template, jsonify
import redis

app = Flask(__name__)

# Redis connection details
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

# Charity quotes list
charity_quotes = [
    "No one has ever become poor by giving. – Anne Frank",
    "Charity sees the need, not the cause. – German Proverb",
    "The best way to find yourself is to lose yourself in the service of others. – Mahatma Gandhi",
    "We make a living by what we get, but we make a life by what we give. – Winston Churchill",
    "Service to others is the rent you pay for your room here on earth. – Muhammad Ali",
    "Give, but give until it hurts. – Mother Teresa"
]

@app.route('/')
def home():
    """
    Render the home page about water issues in Kenya.
    """
    # Facts about water issues
    facts = {
        "drought_areas": "Over 4 million people in Kenya face food and water shortages due to recurring droughts.",
        "rainfall_decline": "Average annual rainfall has dropped by nearly 20% in the last three decades.",
        "population_affected": "About 40% of Kenya’s population lack access to clean and safe water.",
        "climate_change": "Climate change has intensified dry seasons and reduced water sources."
    }
    return render_template('home.html', facts=facts)

@app.route('/count')
def count():
    """
    Increment visitor count and display a random charity quote.
    """
    count = r.incr('visits')
    quote = random.choice(charity_quotes)
    return render_template('count.html', count=count, quote=quote)

@app.route('/count/api')
def count_api():
    """
    API endpoint for current visitor count.
    """
    count = r.get('visits') or 0
    return jsonify({'count': int(count)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)