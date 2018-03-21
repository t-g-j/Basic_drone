#!/usr/bin/env python
#*****************************************************************************
# UTM projection conversion test
# Copyright (c) 2013-2016, Kjeld Jensen <kjeld@frobomind.org>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#*****************************************************************************
"""
This file contains a simple Python script to test the UTM conversion class.

Revision
2013-04-05 KJ First version
2015-03-09 KJ Minor update of the license text.
2016-01-16 KJ Corrected a minor problem with the library location reference.
"""
# import utmconv class
from utm import utmconv
from math import pi, cos, sin, asin, acos, sqrt

# define test position
test_lat =  55.0
test_lon = 009.0
print ('Test position [deg]:')
print ('  latitude:  %.10f'  % (test_lat))
print ('  longitude: %.10f'  % (test_lon))



"""
Defining positions read from google maps 1 km north of the point given in 
UAS lab six and another point 1km east of said point
"""
# ground zero
g_lat = 55.47
g_lon = 010.33
# point 1 - east from ground zero
east_lat = 55.470292
east_lon = 010.346109

# point 2 - north from ground zero
north_lat = 55.479462
north_lon = 010.329887


# instantiate utmconv class
uc = utmconv()

# define functions
def greatCircleFormulae(lat1,lon1,lat2,lon2):
	d = 2*asin(sqrt((sin((lat1-lat2)/2))**2 +cos(lat1)*cos(lat2)*(sin((lon1-lon2)/2))**2))
	#d = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
	return d


########## NOT FINISHED _ TEST SECTION!!!#######
# 2 points from google maps measure in UTM
northing_test = 6148714.23
easting_test = 0584214.47
zone_test = 32
letter_test = 'U'

northing_test_2 = 6148198.76
easting_test_2 = 583357.94
zone_test_2 = 32
letter_test_2 = 'U'

(my_lat,my_lon) = uc.utm_to_geodetic('N',zone_test,easting_test,northing_test)
(my_lat_2,my_lon_2) = uc.utm_to_geodetic('N',zone_test_2,easting_test_2,northing_test_2)
print ('  MY latitude:  %.10f'  % (my_lat))
print ('  MY longitude: %.10f'  % (my_lon))

print ('  MY latitude_2:  %.10f'  % (my_lat_2))
print ('  MY longitude_2: %.10f'  % (my_lon_2))
################################



# convert from geodetic to UTM
(hemisphere, zone, letter, easting, northing) = uc.geodetic_to_utm (test_lat,test_lon)
print ('\nConverted from geodetic to UTM [m]')
print ('  %d %c %.5fe %.5fn' % (zone, letter, easting, northing))



#Converting the two points into UTM
(hemisphere_p1, zone_p1, letter_p1, easting_p1, northing_p1) = uc.geodetic_to_utm (east_lat,east_lon)
(hemisphere_p2, zone_p2, letter_p2, easting_p2, northing_p2) = uc.geodetic_to_utm (north_lat,north_lon)
print ('  %d %c %.5fe %.5fn' % (zone_p1, letter_p1, easting_p1, northing_p1))
print ('  %d %c %.5fe %.5fn' % (zone_p2, letter_p2, easting_p2, northing_p2))


print('\n###############################')



# convert back from UTM to geodetic
(lat, lon) = uc.utm_to_geodetic (hemisphere, zone, easting, northing)
print ('\nConverted back from UTM to geodetic [deg]:')
print ('  latitude:  %.10f'  % (lat))
print ('  longitude: %.10f'  % (lon))




# convert the 2 points back to geodetic
(lat_p1, lon_p1) = uc.utm_to_geodetic (hemisphere_p1, zone_p1, easting_p1, northing_p1)
(lat_p2, lon_p2) = uc.utm_to_geodetic (hemisphere_p2, zone_p2, easting_p2, northing_p2)
print ('------- point 1 east of the airport -------')
print ('  latitude:  %.10f'  % (lat_p1))
print ('  longitude: %.10f'  % (lon_p1))
print ('------- point 2 north of the airport -------')
print ('  latitude:  %.10f'  % (lat_p2))
print ('  longitude: %.10f'  % (lon_p2))

print('\n###############################')

# detrmine conversion position error [m]
lat_err = abs(lat-test_lat)
lon_err = abs(lon-test_lon)
earth_radius = 6378137.0 # [m]
lat_pos_err = lat_err/360.0 * 2*pi*earth_radius
lon_pos_err = lon_err/360.0 * 2*pi*(cos(lat)*earth_radius)
print ('\nPositional error from the two conversions [m]:')
print ('  latitude:  %.10f'  % (lat_pos_err))
print ('  longitude: %.10f'  % (lon_pos_err))

# determine coversion position error [m] in the 2 points
# point 1 east
lat_err_p1 = abs(lat_p1-east_lat)
lon_err_p1 = abs(lon_p1-east_lon)
earth_radius = 6378137.0 # [m]
lat_pos_err_p1 = lat_err_p1/360.0 * 2*pi*earth_radius
lon_pos_err_p1 = lon_err_p1/360.0 * 2*pi*(cos(lat_p1)*earth_radius)
print ('------- point 1 east of the airport -------')
print ('  latitude:  %.10f'  % (lat_pos_err_p1))
print ('  longitude: %.10f'  % (lon_pos_err_p1))
# point 2 north
lat_err_p2 = abs(lat_p2-north_lat)
lon_err_p2 = abs(lon_p2-north_lon)
earth_radius = 6378137.0 # [m]
lat_pos_err_p2 = lat_err_p2/360.0 * 2*pi*earth_radius
lon_pos_err_p2 = lon_err_p2/360.0 * 2*pi*(cos(lat_p2)*earth_radius)
print ('------- point 2 north of the airport -------')
print ('  latitude:  %.10f'  % (lat_pos_err_p2))
print ('  longitude: %.10f'  % (lon_pos_err_p2))

###
print('\n###############################')


print ('\nGreat circle formula distance ')
print(greatCircleFormulae(g_lat*pi/180,g_lon*pi/180,east_lat*pi/180,east_lon*pi/180)*earth_radius)
print('Great circle distance between 1km UTM distance')
print(greatCircleFormulae(my_lat*pi/180,my_lon*pi/180,my_lat_2*pi/180,my_lon_2*pi/180)*earth_radius)