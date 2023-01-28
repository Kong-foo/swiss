
rounds = 4
playernames = ["a", "b", "c", "d"]
listofplayers = [None for x in range(len(playernames))]

def getResultsInto(playerlist, roundnumber):
	return


#sort from lowest to highest score
def sortByRating(playerlist):
	for i in range(0, len(listofplayers), 2):
		if (listofplayers[i+1].level < listofplayers[i].level):
			tmp = listofplayers[i]
			listofplayers[i] = listofplayers[i+1]
			listofplayers[i+1] = tmp
	return

class Player:
	def __init__(self, name):
		global rounds
		self.name = name
		self.level = rounds
		self.playersPlayed = [None for x in range(len(playernames))]

for i in range(0, len(playernames)):
	listofplayers[i] = Player(playernames[i])

roundnumber = 1
print("round "+str(roundnumber))
for i in range(0,len(listofplayers), 2):
	print(listofplayers[i].name, "plays against",listofplayers[i+1].name)
	listofplayers[i].playersPlayed.append(listofplayers[i+1])
	listofplayers[i+1].playersPlayed.append(listofplayers[i])

getResultsInto(listofplayers, roundnumber)
sortByRating(listofplayers)


