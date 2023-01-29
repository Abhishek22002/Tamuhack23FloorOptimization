from typing import List

class team:

    def team(name:str, strength:int, preferred:List[int], tolerated:List[int], no_way:List[int], this:team):
        this.name = name
        this.strength = strength
        this.preferred = preferred
        this.tolerated = tolerated
        this.no_way = no_way