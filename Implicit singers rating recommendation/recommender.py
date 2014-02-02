users2 = {"Amy": {"Taylor Swift": 4, "PSY": 3, "Whitney Houston": 4},
"Ben": {"Taylor Swift": 5, "PSY": 2},
"Clara": {"PSY": 3.5, "Whitney Houston": 4},
"Daisy": {"Taylor Swift": 5, "Whitney Houston": 3}}

class recommender:
	def __init__(self, data, k=1, metric='pearson', n=5):
		self.k = k
		self.n = n
      # The following two variables are used for Slope One
		self.frequencies = {}
		self.deviations = {}
		if type(data).__name__ == 'dict':
			self.data = data
	
	def computeDeviations(self):
		for ratings in self.data.values():
			for (item,rating) in ratings.items():
				self.frequencies.setdefault(item,{})
				self.deviations.setdefault(item,{})
				
				for (item2,rating2) in ratings.items():
					if item!=item2:
						self.frequencies[item].setdefault(item2,0)
						self.deviations[item].setdefault(item2,0.0)
						self.frquencies[item][item2]+=1
						self.deviations[item][item2]+=(rating-rating2)
						
		for (item,ratings) in self.deviations.items():
			for item2 in ratings:
				ratings[item2]/=self.frequencies[item][item2]
				
