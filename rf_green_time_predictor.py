import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

class GreenTimePredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self.model, "rf_green_time_predictor.pkl")

    def load(self):
        self.model = joblib.load("rf_green_time_predictor.pkl")

    def predict(self, X):
        return self.model.predict(X)
