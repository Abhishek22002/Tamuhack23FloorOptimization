from typing import List

class team:

    def __init__(self, name:str, strength:int, preferred:List[int], tolerated:List[int], no_way:List[int]) -> None:
        self.name = name
        self.strength = strength
        self.preferred = preferred
        self.tolerated = tolerated
        self.no_way = no_way