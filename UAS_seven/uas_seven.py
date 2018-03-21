import matplotlib.pyplot as plt
import numpy as np
#a = np.linspace(0,10,100)
#b = np.exp(-a)
#plt.plot(a,b)
#plt.show()

class Route_planning:
	def __init__(self):
		self.data = []
		self.time = []
		self.latitude = []
		self.lontitude = []

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
		for i in range(len(self.data)):
			line = self.data[i]
			self.latitude.append(line[1])
		return self.latitude

	def get_lon(self):
		for i in range(len(self.data)):
			line = self.data[i]
#			self.lontitude.append(line[2])
		#return self.longtitude




if __name__ == "__main__":
	print('Importing file')
	rp = Route_planning()
	rp.import_file('position_inside.log')
	#print(rp.get_time())
	rp.get_lat()
	#print(rp.get_lon())
	print('Done importing')