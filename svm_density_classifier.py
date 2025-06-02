import numpy as np
from sklearn import svm
import joblib

class TrafficDensityClassifier:
    def __init__(self):
        self.model = svm.SVC(kernel='linear', probability=True)

    def train(self, X, y):
        self.model.fit(X, y)
        joblib.dump(self.model, "svm_density_classifier.pkl")

    def load(self):
        self.model = joblib.load("svm_density_classifier.pkl")

    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)
