import matplotlib.pyplot as plt
import numpy as np
from utm import utmconv
from math import pi, cos, sin, asin, acos, sqrt

#a = np.linspace(0,10,100)
#b = np.exp(-a)
#plt.plot(a,b)
#plt.show()

# instantiate utmconv class
uc = utmconv()

class Route_planning:
	def __init__(self):
		self.data = []
		self.line = []
		self.time = []
		self.latitude = []
		self.lat =[]
		self.lon =[]
		self.longtitude = []
		self.altitude =[]
		self.relative_alt=[]
		self.hem=[]
		self.zo=[]
		self.let=[]
		self.east=[]
		self.north=[]


	def import_file(self, file_name):
		file_ok = True
		try:
			# read all lines from the file and strip \n
			lines = [line.rstrip() for line in open(file_name)]
		except:
			file_ok = False
		if file_ok == True:
			pt_num = 0
			for i in range(len(lines)):  # for all lines
				if len(lines[i]) > 0 and lines[i][0] != '#':  # if not a comment or empty line
					csv = lines[i].split(',')  # split into comma separated list
					self.data.append(csv)
					#print(len(self.data) )

	def get_time(self):
		for i in range(len(self.data)):
			line = self.data[i]
			self.time.append(line[0])
		return self.time

	def get_lat(self):
		for i in self.data:
			#print(i)
			if len(i) == 9:
				self.latitude.append(i[1])
			#print(self.latitude)
		return self.latitude

	def get_lon(self):
		for i in self.data:
			if len(i) == 9:
				self.longtitude.append(i[2])
		return self.longtitude

	def alt(self):
		for i in self.data:
			if len(i) == 9:
				self.altitude.append(i[2])
		return self.altitude

	def rel_alt(self):
		for i in self.data:
			if len(i) == 9:
				self.relative_alt.append(i[2])
		return self.relative_alt

	def conv_2_float(self,list):
		[float(i) for i in list]
		return list

	def conv_lat_lon_lists(self):
		# convert from geodetic to UTM
		self.lat = rp.conv_2_float(self.latitude)
		self.lon = rp.conv_2_float(self.longtitude)
		#print(tmp)
		#print(tmp2)
		print('\nConverted from geodetic to UTM [m]')
		it = len(self.latitude)
		print(it)
		for x in range(it):
			tmp = self.lat[x]
			tmp2 = self.lon[x]
			(hemisphere, zone, letter, easting, northing) = uc.geodetic_to_utm(float(tmp),float(tmp2))
			self.hem.append(hemisphere)
			self.zo.append(zone)
			self.let.append(letter)
			self.east.append(easting)
			self.north.append(northing)
			#print('  %d %c %.5fe %.5fn' % (zone, letter, easting, northing))

	def remove_outliers(self):
		 a = np.linspace(0,10,100)
		 b = np.exp(-a)
		 plt.plot(self.east,self.north)
		 plt.axis('equal')
		 plt.show()


if __name__ == "__main__":
	print('Importing file')
	rp = Route_planning()
	#rp.import_file('position_tekbuilding.log')
	rp.import_file('position_last_walk.log')
	print('Done importing')
	print("----- Time -------")
	print(rp.get_time())
	print("\n----- Latitude -------")
	print(rp.get_lat())
	print("\n----- Longtitude -------")
	print(rp.get_lon())
	rp.conv_lat_lon_lists()
	rp.remove_outliers()