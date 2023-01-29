from typing import List

class floor():

    def __init__(self, name:str, max_capacity:int) -> None:
        self.name = name
        self.max_capacity = max_capacity

class team():

    def __init__(self, name:str, strength:int, preferred:List[int], tolerated:List[int], no_way:List[int]) -> None:
        self.name = name
        self.strength = strength
        self.preferred = preferred
        self.tolerated = tolerated
        self.no_way = no_way

class Algo():

    def __init__(self, teamList:List[team], floorList:List[floor]) -> None:
        print("test")

