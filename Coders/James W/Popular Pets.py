import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Animals'
piechart.add('Rabbits',90)
piechart.add('Hamsters',85)
piechart.add('Dogs',100)
piechart.add('Cats',100)
piechart.render()





file = open('pets.txt', 'r')
for line in file.read().splitlines():
  print(line)
  
  file.close()
