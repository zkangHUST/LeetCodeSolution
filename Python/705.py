class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucketsize = 7
        self.table = [[], [], [], [], [], [], []]

    def add(self, key: int) -> None:
        index = key % self.bucketsize
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.bucketsize
        if key in self.table[index]:
            self.table[index].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.bucketsize
        if key in self.table[index]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)