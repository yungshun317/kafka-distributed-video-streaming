import datetime
from flask import Flask, Response, render_template
from kafka import KafkaConsumer

topic = "testing"

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed', methods=['GET'])
def video_feed():
    return Response(get_video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
