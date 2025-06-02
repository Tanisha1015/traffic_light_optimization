import numpy as np
import pandas as pd
import time
from datetime import datetime
from mongodb_utils import insert_traffic_record
from svm_density_classifier import TrafficDensityClassifier
from rf_green_time_predictor import GreenTimePredictor

# Simulate lane features: [vehicle_count, avg_speed, is_peak_hour]
def generate_lane_features():
    vehicle_count = np.random.randint(1, 50)
    avg_speed = np.random.uniform(10, 60)  # km/h
    is_peak_hour = np.random.choice([0, 1])
    return np.array([[vehicle_count, avg_speed, is_peak_hour]])

def main():
    # Load pre-trained models
    density_clf = TrafficDensityClassifier()
    density_clf.load()
    green_time_pred = GreenTimePredictor()
    green_time_pred.load()

    while True:
        features = generate_lane_features()
        density = density_clf.predict(features)[0]  # 1 = high, 0 = low
        green_time = int(green_time_pred.predict(features)[0])
        record = {
            "timestamp": datetime.now(),
            "vehicle_count": int(features[0, 0]),
            "avg_speed": float(features[0, 1]),
            "is_peak_hour": int(features[0, 2]),
            "density": int(density),
            "green_time": green_time
        }
        insert_traffic_record(record)
        print(f"Inserted: {record}")
        time.sleep(5)  # Simulate every 5 seconds

if __name__ == "__main__":
    main()
