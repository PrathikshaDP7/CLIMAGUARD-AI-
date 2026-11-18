
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    sensor_data = {
        "temperature": 28,
        "humidity": 65,
        "soil_moisture": 42,
        "rainfall": "No Rain",
        "status": "Monitoring"
    }

    return render_template("index.html", data=sensor_data)


@app.route("/api/sensors")
def get_sensor_data():

    sensor_data = {
        "temperature": round(random.uniform(25, 38), 1),
        "humidity": round(random.uniform(40, 85), 1),
        "soil_moisture": round(random.uniform(20, 70), 1),
        "rainfall": random.choice(["Rain", "No Rain"])
    }

    return jsonify(sensor_data)


if __name__ == "__main__":
    app.run(debug=True)
