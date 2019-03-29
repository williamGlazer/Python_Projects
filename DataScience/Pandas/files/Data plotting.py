# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# Loads flights dataset, run once
flights = pd.read_csv('flights.csv', index_col=False)

# Plot histogram of expected de times
# Hours 2010 -> 20:10
flights['CRS_DEP_TIME'].hist()

# Plot histogram of expected dep/arr times
# Hours 2010 -> 20:10
flights['CRS_DEP_TIME'].hist()
flights['ARR_TIME'].hist()

# Plot aggregate data
flights_by_month = flights.groupby('MONTH')
flights_by_month['DISTANCE'].aggregate(np.sum).plot()

flights_by_day = flights.groupby('DAY_OF_WEEK')
flights_by_day['DISTANCE'].aggregate(np.sum).plot()