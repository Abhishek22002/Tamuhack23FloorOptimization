from typing import List

class floor():

    def __init__(self, name:str, maxCapacity:int) -> None:
        self.name = name
        self.maxCapacity = maxCapacity

class team():

    def __init__(self, name:str, strength:int, preferred:List[int], tolerated:List[int], noWay:List[int]) -> None:
        self.name = name
        self.strength = strength
        self.preferred = preferred
        self.tolerated = tolerated
        self.noWay = noWay

class Algo():

    def __init__(self, teamList:List[team], floorList:List[floor]) -> None:
        print("test")

