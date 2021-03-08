class Bucket:
    def __init__(self):
        self.bucket = []
        
    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        flag = False
        for i, d in enumerate(self.bucket):
            if d[0] == key:
                self.bucket[i] = (key, value)
                flag = True
                break
        
        if not flag:
            self.bucket.append((key, value))
    
    def remove(self, key):
        for i, d in enumerate(self.bucket):
            if key == d[0]:
                del self.bucket[i]

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.space = 2069
        self.hashtable = [Bucket() for i in range(self.space)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = key % self.space
        self.hashtable[hash_key].update(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = key % self.space
        return self.hashtable[hash_key].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = key % self.space
        self.hashtable[hash_key].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
