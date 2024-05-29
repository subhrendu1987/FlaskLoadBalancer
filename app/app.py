# Importing Flask Python micro web framework
from flask import Flask
import time
import random
import os

app = Flask(__name__)

# This is a Flask application route
@app.route("/")
def load_balancing():
    # Introduce a random delay between 1 and 5 seconds
    delay = random.randint(1, 5)
    time.sleep(delay)

    # Get the container name from the environment variable
    container_name = os.environ.get('CONTAINER_NAME', 'unknown container')
    
    return f"<p><h3>Flask Application Load Balancing using Docker Compose and Nginx</h3></p><p>Response from {container_name}</p><p>Delayed by {delay}s </p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)