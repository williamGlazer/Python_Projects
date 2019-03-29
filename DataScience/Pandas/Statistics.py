# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Loads flights dataset, run once
flights = pd.read_csv('flights.csv', index_col=False)

# Statistics
print(flights.describe())

# compute mean and sd of DIST
flights['DISTANCE'].mean()
flights['DISTANCE'].std()

# Mean of Delta CRSdep and dep
(flights['DEP_TIME']-flights['CRS_DEP_TIME']).describe()

# SubArray
flights_subsample = flights.sample(1000)

# Plot
plt.scatter(flights_subsample['DISTANCE'],flights_subsample['CRS_ELAPSED_TIME'])

# Perform LinReg
slope, intercept, r_value, _, _ = linregress(flights_subsample['DISTANCE'],flights_subsample['CRS_ELAPSED_TIME'])
print('y = {}x + {}; r = {}'.format(slope, intercept, r_value))

# Generate x value to feed to line
x = np.linspace(flights_subsample['DISTANCE'].min(), flights_subsample['DISTANCE'].max(), 1000)
y = slope*x + intercept
plt.plot(x,y, 'r--')
plt.show()

# Use slope & intercept for prediction
distance = 5000
flight_time = slope*distance + intercept
print(flight_time)
