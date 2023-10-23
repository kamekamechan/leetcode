import random
class RandomizedSet:

    def __init__(self):
        self.num_list = {}

    def insert(self, val: int) -> bool:
        if(str(val) not in self.num_list.keys()):
            self.num_list[str(val)] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if(str(val) in self.num_list.keys()):
            del self.num_list[str(val)]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return_index = random.randint(0, len(self.num_list.keys()) - 1)
        return self.num_list[list(self.num_list.keys())[return_index]]


obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
print(obj.num_list.keys())
print(obj.getRandom())
obj.remove(1)
print(obj.num_list)
obj.insert(2)
print(obj.getRandom())
print(obj.num_list)