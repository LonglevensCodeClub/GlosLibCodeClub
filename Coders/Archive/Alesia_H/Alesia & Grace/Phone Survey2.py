#!/bin/python3

import pygal

barchart = pygal.Bar()
barchart.title = 'Phone Brands'
barchart.add('Apple' , 3)
barchart.add('Samsung' , 2)
barchart.add('Huawei' , 3)
barchart.add('Moto G' , 1)
barchart.add('No Phone' , 1)
barchart.add('Microsoft' , 2)
barchart.render()
