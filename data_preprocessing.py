import pandas as pd
import numpy as np

def moving_average_filter(data, window_size=5):
    return data.rolling(window=window_size, min_periods=1).mean()

def impute_missing(data):
    return data.interpolate(method='linear', limit_direction='both')
