#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as p
import pickle


'''
Columns
'''


# Load data
with open('fruit-sales.pickle', 'rb') as f:
    data = pickle.load(f)
    
# Split tuples from (name, number) to 2 lists
fruit, num_sold = zip(*data)

# coords
bar_coords = range(len(fruit))

# Settings & plot
p.xticks(bar_coords, fruit)
p.bar(bar_coords, num_sold)
p.ylabel('Number of Fruits (millions)')
p.title('Number of Fruits Sold (2017)')
p.show()

p.clf()
p.cla()


'''
Rows
'''
# Load data
with open('coding-exp-by-dev-type.pickle', 'rb') as f:
    data = pickle.load(f)

# Split tuples from (name, number) to 2 lists
dev_types, years_exp = zip(*data)

# coords
bar_coords = range(len(dev_types))

# Settings & plot
p.yticks(bar_coords, dev_types)
p.barh(bar_coords, years_exp)
p.xlabel('Years')
p.title('Year of Coding Experience by Developper Type')
p.tight_layout()
p.show()

p.clf()
p.cla()


'''
Pie Chart
'''
# Load data
with open('devs-outside-time.pickle', 'rb') as f:
    data = pickle.load(f)

# Split tuples from (name, number) to 2 lists
time, responses = zip(*data)

# Settings & plot
p.pie(responses, labels=time, autopct='%d%%')
p.axis('equal')
p.title('Daliy Time Developpers Spend Outside')
p.tight_layout()
p.show()

p.clf()
p.cla()




'''
Line
'''
# Load data
with open('prog-langs-popularity.pickle', 'rb') as f:
    data = pickle.load(f)

# Split tuples from (name, number) to 2 lists
language, rankings = zip(*data)
java_years, java_rank = zip(*rankings[0])

# Settings & plot
p.plot(java_years, java_rank)
p.xticks(java_years)
p.xlabel('Year')
p.ylabel('Ranking')
p.title('Java Ranking')
p.tight_layout()
p.show()

p.clf()
p.cla()

'''
Multiple Lines
'''

for i in range(len(language)):
    years, ranks = zip(*rankings[i])
    p.plot(years,ranks)

p.xlabel('Year')
p.ylabel('Ranking')
p.title('Rankings of Programming Languages')
p.tight_layout()
p.legend(language)
p.show()

p.clf()
p.cla()




'''
Scatter
'''
# Load data
with open('iris.pickle', 'rb') as f:
    iris = pickle.load(f)

# Split tuples from (name, number) to 2 lists
sepal_length = iris['data'][:,0]
sepal_width  = iris['data'][:,1]
classes      = iris['target']

# Settings & plot
p.scatter(sepal_length, sepal_width, c=classes)
p.xlabel('Sepal Length (cm)')
p.ylabel('Sepal Width (cm)')
p.title('Iris Data : Sepal length Vs. width')
p.tight_layout()
p.show()

p.clf()
p.cla()




'''
MULTI
'''
# Load data
with open('iris.pickle', 'rb') as f:
    iris = pickle.load(f)

# Split tuples from (name, number) to 2 lists
sepal_length = iris['data'][:,0]
sepal_width  = iris['data'][:,1]
petal_length  = iris['data'][:,2]
petal_width  = iris['data'][:,3]
classes      = iris['target']

# Settings & plot
fig, axes = p.subplots(2,2)

axes[0,0].scatter(sepal_length,sepal_width,c=classes)
axes[0,0].set_xlabel('Sepal Length (cm)')
axes[0,0].set_xlabel('Sepal Width (cm)')

axes[0,1].scatter(petal_length,petal_width,c=classes)
axes[0,1].set_xlabel('Petal Length (cm)')
axes[0,1].set_xlabel('Petal Width (cm)')

axes[1,0].scatter(sepal_length,petal_length,c=classes)
axes[1,0].set_xlabel('Sepal Length (cm)')
axes[1,0].set_xlabel('Petal Length (cm)')

axes[1,1].scatter(sepal_width,petal_width,c=classes)
axes[1,1].set_xlabel('Sepal Width (cm)')
axes[1,1].set_xlabel('Petal Width (cm)')

p.tight_layout()
p.show()
