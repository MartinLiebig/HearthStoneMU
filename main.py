import random

filePath = 'C:\\Users\\MartinSchmitz\\PycharmProjects\\HearthStoneMU\\data\\03_09_18'

counter = 0;
class MatchUp:
    firstClass = ""
    secondClass = ""
    winRate = 0.5
    def __init__(self, firstClass, secondClass, winRate):
        self.firstClass = firstClass
        self.secondClass = secondClass
        self.winRate = winRate;

    def __str__(self):
        #return self.secondClass
        return self.firstClass + " - " + self.secondClass + " "+str(self.winRate)
def getListOfWinrates():
    with open(filePath) as f:
        first = ""
        second = ""
        rate = 0.5
        winrates = []
        counter = 0
        for x in f:
            if (x == "" or x.strip() == "Mirror matchup"):
                counter = 0
            elif(x != "" and x.strip() != "Mirror matchup"):

                if(counter == 0):
                    #print("First Class",x)
                    first = x.replace("\n","").strip()
                elif(counter ==1):
                    #print("Second Class",x.replace("Versus: ",""))
                    second = x.replace("Versus:","").replace("\n","").strip()
                elif(counter ==2):
                    #print("Winrate",x.replace("Winrate:","").replace("%",""))
                    rate = float(x.replace("Winrate:","").replace("%",""))/100
                counter+=1;
                if(counter > 4):
                    winrates.append(MatchUp(first,second,rate))
                    counter = 0;
    return winrates

def getSingeWR(classOne, classTwo, listofWR):
    if(classOne == classTwo):
        return 0.5
    for wr in listofWR:
        if(wr.firstClass == classOne and wr.secondClass == classTwo):
            return wr.winRate
    print("Cant find MU",classOne,classTwo)

if __name__ == "__main__":
    winrates = getListOfWinrates()

    winOne = 0
    winTwo = 0
    iterations = 100000;
    for i in range(iterations):
        #print(i)
        listOne = ["Control Warlock", "Odd Warrior", "Malygos Druid"]
        listTwo = ["Zoo Warlock", "Tempo Mage", "Odd Rogue"]
        while(len(listOne)>0 and len(listTwo)>0):
            firstClass = random.choice(listOne)
            secondClass = random.choice(listTwo)
            odds = getSingeWR(firstClass,secondClass,winrates)
            #print(odds)
            if(odds <= random.uniform(0,1)):
                listOne.remove(firstClass)
            else:
                listTwo.remove(secondClass)
            if(len(listOne)==0):
                winTwo+=1
            elif(len(listTwo)==0):
                winOne+=1
            #print(winOne)

    print(winTwo/iterations)
    #print(getSingeWR("Even Warlock","Zoo Warlock",winrates))

    # for wr in winrates:
    #    print(wr)
    #
    #
    # print(len(winrates))