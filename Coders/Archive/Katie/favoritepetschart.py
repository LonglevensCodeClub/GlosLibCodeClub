#!/bin/python3

import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pets!'
piechart.add('Dog',11 )
piechart.add('cat',10 )
piechart.add('Lizard', 1)
piechart.add('Hampster', 1)
piechart.add('Budgie', 1)
piechart.add('Turtle', 1)
piechart.add('Horse', 2)
piechart.render()

#27
