from flask import Flask, jsonify, render_template
from mongodb_utils import get_latest_records

app = Flask(__name__)

@app.route("/api/traffic")
def traffic_data():
    records = get_latest_records(10)
    for r in records:
        r["timestamp"] = r["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        r["_id"] = str(r["_id"])
    return jsonify(records)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
