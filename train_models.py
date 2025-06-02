import numpy as np
import pandas as pd
from svm_density_classifier import TrafficDensityClassifier
from rf_green_time_predictor import GreenTimePredictor

# Generate synthetic training data
np.random.seed(42)
N = 500
vehicle_count = np.random.randint(1, 50, N)
avg_speed = np.random.uniform(10, 60, N)
is_peak_hour = np.random.choice([0, 1], N)

# Density label: high (1) if vehicle_count > 25 or is_peak_hour and avg_speed < 30
density = ((vehicle_count > 25) | ((is_peak_hour == 1) & (avg_speed < 30))).astype(int)

# Green time: more for high density, less for low
green_time = 30 + 1.5 * vehicle_count - 0.4 * avg_speed + 10 * is_peak_hour + np.random.normal(0, 3, N)
green_time = np.clip(green_time, 15, 120)

X = np.stack([vehicle_count, avg_speed, is_peak_hour], axis=1)
y_density = density
y_green = green_time

# Train and save SVM density classifier
density_clf = TrafficDensityClassifier()
density_clf.train(X, y_density)

# Train and save Random Forest regressor for green time
green_time_pred = GreenTimePredictor()
green_time_pred.train(X, y_green)

print("Models trained and saved!")
