#https://leetcode.com/problems/design-hashmap/
class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.length = 1000
        self.arr = [Node() for i in range(self.length)]

    def hash(self, key :int) -> int:
        return ke y %self.length

    def put(self, key: int, value: int) -> None:
        pos = self.hash(key)
        current = self.arr[pos]
        while current.next:
            if current.next.key == key:
                current.next.val = value
                return
            current = current.next
        current.next = Node(key=key, val=value)

    def get(self, key: int) -> int:
        pos = self.hash(key)
        current = self.arr[pos]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        pos = self.hash(key)
        current = self.arr[pos]
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)