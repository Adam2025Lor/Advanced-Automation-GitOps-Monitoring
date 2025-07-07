from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a Prometheus metric (a simple counter)
REQUEST_COUNT = Counter("quakewatch_requests_total", "Total requests to QuakeWatch")

@app.route('/')
def index():
    REQUEST_COUNT.inc()  # Increment metric on every visit
    return 'Quakewatch is on!'

# Expose metrics on /metrics endpoint
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
