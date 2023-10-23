class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_dict = {}

    def get(self, key: int) -> int:
        if(key in self.value_dict.keys()):
            return_value = self.value_dict[key]
        else:
            return -1
        del self.value_dict[key]
        self.value_dict[key] = return_value
        return return_value 

    def put(self, key: int, value: int) -> None:
        key_list = self.value_dict.keys()
        if(key in key_list):
            del self.value_dict[key]
            self.value_dict[key] = value
        else:
            if(len(key_list) == self.capacity):
                del self.value_dict[next(iter(self.value_dict))]
            self.value_dict[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)