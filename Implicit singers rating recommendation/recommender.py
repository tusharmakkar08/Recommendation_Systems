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
		self.productid2name = {}
		if type(data).__name__ == 'dict':
			self.data = data
	def convertProductID2name(self, id):
		if id in self.productid2name:
			return self.productid2name[id]
		else:
			return id
	def computeDeviations(self):
		for ratings in self.data.values():
			for (item,rating) in ratings.items():
				self.frequencies.setdefault(item,{})
				self.deviations.setdefault(item,{})
				
				for (item2,rating2) in ratings.items():
					if item!=item2:
						self.frequencies[item].setdefault(item2,0)
						self.deviations[item].setdefault(item2,0.0)
						self.frequencies[item][item2]+=1
						self.deviations[item][item2]+=(rating-rating2)
		#print self.frequencies.items()
		#print self.deviations.items()
		for (item,ratings) in self.deviations.items():
			for item2 in ratings:
				ratings[item2]/=self.frequencies[item][item2]

	def slopeOneRecommendations(self,userRatings):
		recommendations={}
		frequencies={}
		for (userItem,userRating) in userRatings.items():
			for (diffItem,diffRatings) in self.deviations.items():
				if diffItem not in userRatings and userItem in self.deviations[diffItem]:
					freq=self.frequencies[diffItem][userItem]
					recommendations.setdefault(diffItem,0.0)
					frequencies.setdefault(diffItem,0)
				
					recommendations[diffItem]+=(diffRatings[userItem]+userRating)*freq
					frequencies[diffItem]+=freq
		recommendations =[(self.convertProductID2name(k),v / frequencies[k])for (k, v) in recommendations.items()]
		recommendations.sort(key=lambda artistTuple: artistTuple[1],reverse = True)
		return recommendations
		
					
#r = recommender(users2)
#r.computeDeviations()
#g = users2['Ben']
#print r.slopeOneRecommendations(g)
