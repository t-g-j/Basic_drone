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
		self.maxVel = 20 # m/s
		self.removedOutliers_east = []
		self.removedOutliers_north =[]


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
			#print(rp.greatCircleFormulae(float(self.lat[x]),float(self.lon[x]),float(self.lat[x-1]),float(self.lon[x-1])))
			self.hem.append(hemisphere)
			self.zo.append(zone)
			self.let.append(letter)
			self.east.append(easting)
			self.north.append(northing)
			#print('  %d %c %.5fe %.5fn' % (zone, letter, easting, northing))

	def remove_outliers(self):
		acumu_t=0
		dt=0
		diff_t=0
		#a = np.linspace(0,10,100)
		#b = np.exp(-a)
		it = len(self.north)
		for i in range(it):
			if i == 0:
				#print('test')
				dt+=0
			else:
				acumu_t+=float(self.time[i])-float(self.time[i-1])
				diff_t = float(self.time[i])-float(self.time[i-1])
				(utm_diff_east, utm_diff_north) = self.east[i]-self.east[i-1],self.north[i]-self.north[i-1]
				#print(utm_diff_east,utm_diff_north)
				distance = sqrt(utm_diff_north**2 + utm_diff_east**2)
				#print(distance)
				m_pr_sec = distance/diff_t
				km_pr_hour = m_pr_sec *3.6

				if m_pr_sec < self.maxVel:
					self.removedOutliers_east.append(self.east[i])
					self.removedOutliers_north.append(self.north[i])
			#print(dt)
			#print(diff)
		print(len(self.removedOutliers_north),len(self.north))

		plt.plot(self.removedOutliers_east,self.removedOutliers_north)
		plt.axis('equal')
		plt.show()

	def greatCircleFormulae(self,lat1, lon1, lat2, lon2):
		tmp1 = lat1* pi / 180
		tmp2 =lon1* pi / 180
		tmp3 = lat2 * pi/180
		tmp4 = lon2 *pi/180
		d = 2 * asin(sqrt((sin((tmp1 - tmp3) / 2)) ** 2 + cos(tmp1) * cos(tmp3) * (sin((tmp2 - tmp4) / 2)) ** 2))
		# d = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
		return d

	def simplify_track(self):


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

	# greatCircleFormulae(g_lat * pi / 180, g_lon * pi / 180, east_lat * pi / 180, east_lon * pi / 180) * earth_radius