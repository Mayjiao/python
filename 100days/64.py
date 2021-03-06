#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North,Center, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('na_populations.svg')
