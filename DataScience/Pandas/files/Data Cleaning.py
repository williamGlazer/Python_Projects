# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# Loads flights dataset, run once
flights = pd.read_csv('flights.csv', index_col=False)


# FL_DATE returns object instead of native data type
# yyyy-mm-dd -> pandas date object
flights['FL_DATE'] = pd.to_datetime(flights['FL_DATE'])

# CANCELLED & DIVERTED
# from float64 to bool
flights['CANCELLED'] = flights['CANCELLED'].astype(np.bool)
flights['DIVERTED']  = flights['DIVERTED'].astype(np.bool)

# YEAR MONTH DAY_OF_MONTH & FL_DATE are redundant
# inplace modifies object instead of returning new one
flights.drop(columns=['YEAR','MONTH','DAY_OF_MONTH'], inplace=True)

# rename columns
flights.rename(columns={'DEST':'DESTINATION'}, inplace=True)

# get number of null per columns
print(flights.isnull().sum())
# Difference in CRS dep time & actual de time
# Illustrate null propagation in results
print(flights['CRS_DEP_TIME']-flights['DEP_TIME'])
# Other alternative drop null
print((flights['CRS_DEP_TIME']-flights['DEP_TIME']).dropna())
