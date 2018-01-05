import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('data/air_visit_data.csv')

print(train.shape)
print(train.columns)