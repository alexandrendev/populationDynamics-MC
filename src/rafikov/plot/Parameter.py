import numpy as np

class Parameter:
    def __init__(self, values: np.ndarray, label: str):
        self.label = label
        self.values = values
