from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Tushar'

if __name__ == "__main__":
    # Get the port from environment variable provided by Render
    port = int(os.environ.get('PORT', 5000))  # fallback to 5000 for local testing
    app.run(host='0.0.0.0', port=port)
