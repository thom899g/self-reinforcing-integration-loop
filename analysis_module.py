from typing import Dict, Any
import logging
from sklearn import anomaly_detection
from tensorflow.keras import models

class AnalysisModule:
    def __init__(self):
        self.anomaly_model = models.load_model('anomaly_detection_model.h5')