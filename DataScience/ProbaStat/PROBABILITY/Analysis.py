#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as p
flights = p.read_csv('flights.csv', index_col=False).dropna()


# p(flight started in California)
num_flights_CA = (flights['ORIGIN_STATE_NM'] == 'California').sum()
total_flights  = len(flights)
print('p(flights started in CA) = {}'.format(num_flights_CA/total_flights))

# p(flights started in X) for all state X
flights_states = flights.groupby('ORIGIN_STATE_NM')
num_flights_per_state = flights_states.size()
flight_state_prob = num_flights_per_state.apply(lambda num_flights: num_flights / total_flights)
flight_state_prob.sort_values(inplace = True)
print(flight_state_prob*100)


# p(flight ends in NY | flights started in CA)
flights_start_CA = flights['ORIGIN_STATE_NM'] == 'California'
num_flights_end_NY_start_CA = (flights_start_CA) & (flights['DEST_STATE_NM'] == 'New York')
print(num_flights_end_NY_start_CA.sum() / flights_start_CA.sum() *100)

# p(flight ends in X | flights started in Y) for all X,Y
flight_states = flights.groupby('ORIGIN_STATE_NM')
num_flights_per_state = flight_states['DEST_STATE_NM'].value_counts()
state_counts = flight_states['DEST_STATE_NM'].count()

flight_dist = num_flights_per_state / state_counts
print(flight_dist*100)
