from typing import List

class floor():

    def __init__(self, name:int, maxCapacity:int) -> None:
        self.name = name
        self.maxCapacity = maxCapacity

class team():

    def __init__(self, name:int, strength:int, preferred:List[int], tolerated:List[int], noWay:List[int]) -> None:
        self.name = name
        self.strength = strength
        self.preferred = preferred
        self.tolerated = tolerated
        self.noWay = noWay

class Algo():

    def __init__(self, teamList:List[team], floorList:List[floor]) -> None:
        numPeople = 0 
        for team in teamList:
            numPeople += team.strength

        numCapacity = 0    
        for floor in floorList:
            numCapacity += floor.maxCapacity
        
        print(numPeople, numCapacity)

def removeNoWay(teamList:List[team]) -> List[team]:
    for team in teamList:
        for avoidance in team.noWay:
            try:
                print(teamList[avoidance - 1].preferred.remove(avoidance))
            except:
                print("At team", team.name, "the avoidance of", avoidance, "is not valid")
        
    
    return teamList
                
#Teams
teamOne = team(1, 22, [2,4,6,11], [3,8,10], [5,7,9])
teamTwo = team(2, 45, [1,3,5], [6,7,11], [4,8,9,10])
teamThree = team(3, 34, [1,2,11], [7], [4,5,6,8,9,10])
teamFour = team(4, 51, [10], [1,3], [2,5,6,7,8,9,11])
teamFive = team(5, 11, [1,2,3,4], [9,10,11], [6,7,8])
teamSix = team(6, 37, [7,10], [1,8], [2,3,4,5,9,11])
teamSeven = team(7, 42, [1,2,3,4,5,6], [10,11], [8,9])
teamEight = team(8, 16, [1,10], [2,4,11], [3,5,6,7,9])
teamNine = team(9, 29, [1,5], [2,10], [3,4,6,7,8,11])
teamTen = team(10, 56, [2,6,7,11], [4,5,8], [1,3,9])
teamEleven = team(11, 49, [1,4,5], [2,3,6,7,9,10], [8])

#Floors
floorOne = floor(1, 43)
floorTwo = floor(2, 81)
floorThree = floor(3, 73)
floorFour = floor(4, 54)
floorFive = floor(5, 97)

floors = [floorOne,floorTwo,floorThree,floorFour,floorFive]
teams = [teamOne,teamTwo,teamThree,teamFour,teamFive,teamSix,teamSeven,teamEight,teamNine,teamTen,teamEleven]

Algo(teams,floors)