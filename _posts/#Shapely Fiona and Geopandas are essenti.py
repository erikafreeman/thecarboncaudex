#Shapely Fiona and Geopandas are essential Python tools for geospatial programming. 
#One can use them instead of the ESRI suite of softwares and toolchains. They are free, stable, and best of all: free. 

#File formats 
#Shapefiles are the lingua franca of the geospatial realm. Shapefiles suck [http://switchfromshapefile.org/]. This is an objectively bad format, though no alternative format has 
#really overthrown the Shapefile hegemony. 

#Geopandas does not work for GPX files. You don't even get an error message. Instead of monkey patching Geopandas one can use 
#fiona. 

#Create an environment using a collection of geospatial tools. I really recommend https://github.com/giswqs/python-geospatial

import fiona
from shapely.geometry import shape

import matplotlib.pyplot as plt

import cartopy
from cartopy.io import shapereader
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


fname = '/run/media/erika/GARMIN/Garmin/GPX/Track_CONTROL2.gpx'
print(fiona.listlayers(fname))
layer = fiona.open(fname, layer = 'tracks')
print(len(list(layer.items())))
geom = layer[0]
print(type(geom))
print(geom.keys())
print(geom['type'], geom['id'], geom['properties'])
data = {'type': 'MultiLineString', 'coordinates': geom['geometry']['coordinates']}
shp = shape(data)
