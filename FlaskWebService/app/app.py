# Importing Flask Python micro web framework
from flask import Flask
app = Flask(__name__)
# This is a Flask application route
@app.route("/")

# This is a FLask application function
def load_balancing():
    return "<p><h3>Flask Application Load Balancing using Docker Compose and Nginx<h3></p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)