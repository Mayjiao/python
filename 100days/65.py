#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygal_maps_world.maps
import json
from country_codes import get_country_code

cc_populations = {}
with open('country_population.csv', 'r') as f:
   for line in f.readlines():
       datas = line.split(',')       
       countryCode = get_country_code(datas[0].strip('"'))
       squan = datas[-3].strip().strip('"')
       if (squan.isdigit()):
           quantity    = int(squan)
           cc_populations[countryCode] = quantity
       else:
           continue

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
 
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2017, by Country'
#wm.add('2017', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('World_population.svg')
