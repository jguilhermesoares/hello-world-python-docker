"""
Flask Hello World Application

A simple Flask web application that returns a Hello World message.
Designed to run on port 8081 for EKS deployment.
"""

from flask import Flask

# Create Flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Return a simple Hello World message."""
    return "Hello World from Python Flask!"

@app.route('/health')
def health_check():
    """Health check endpoint for load balancer."""
    return {"status": "healthy", "message": "Application is running"}, 200

@app.route('/oms/marketplace/mgmt/health/liveness')
def liveness_probe():
    """Kubernetes liveness probe endpoint."""
    return {"status": "alive", "message": "Application is alive"}, 200

if __name__ == '__main__':
    # Run the Flask development server
    # In production, this should be run with a proper WSGI server like Gunicorn
    app.run(host='0.0.0.0', port=8000, debug=True)