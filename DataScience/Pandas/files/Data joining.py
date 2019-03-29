# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

# Loads flights dataset, run once
flights = pd.read_csv('flights.csv', index_col=False)

# Load mapping CSV file
days_of_week = pd.read_csv('L_WEEKDAYS.csv', index_col=False)

# Merge two dataframes
merged_df = pd.merge(flights, days_of_week, left_on='DAY_OF_WEEK', right_on='Code')

# reomve DAY_OF_WEEK & Code Columns
# inplace modifies object instead of returning new one
merged_df.drop(columns=['DAY_OF_WEEK','Code'], inplace=True)

# description -> day_of_week
merged_df.rename(columns={'Description':'DAY_OF_WEEK'}, inplace=True)