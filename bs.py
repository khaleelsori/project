import dataset

dataB = dataset.connect('sqlite:///dataB.db' )
table = dataB["users"]
dataB.begin()

def insertBird(name, img,video,description):
	try:
		print("add")
		table.insert(dict(name=name, img=img,video=video,description=description ))
    		dataB.commit()
	except:
	   	 dataB.rollback()

def getBirds():
	 print(table.all())
	 return table.all()

def GetBird(name1):
	return table.find_one(name=name1)



