import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pets!'
piechart.add('Dog',7 )
piechart.add('cat',6 )
piechart.add('Lizard', 1)
piechart.add('Hampster', 1)
piechart.add('Budgie', 1)
piechart.add('Turtle', 1)
piechart.render()

#17
