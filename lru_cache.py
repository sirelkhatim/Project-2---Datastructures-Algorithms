### data structure to store key, value, times used
from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.lru = deque()
        self.capacity = capacity

    def set_lru_capacity(self):
        if len(self.lru)>self.capacity:
            self.lru.popleft()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            self.lru.append(key)
            self.set_lru_capacity()
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            return None
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.lru)<self.capacity:
            self.cache[key] = value
            self.lru.append(key)
            self.set_lru_capacity()     
        else:
            key_min_value = self.lru.popleft()
            self.cache.pop(key_min_value,None)
            self.cache[key] = value
            self.lru.append(key)
            self.set_lru_capacity()






# Test 1:
print("Test 1: ")
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Test 2: repeated values
print('Test 2: ')
our_cache = LRU_Cache(5)

our_cache.set(1,1)
our_cache.set(2,1)
our_cache.set(3,1)
our_cache.set(4,1)
our_cache.set(5,1)

print(our_cache.get(3))

our_cache.set(6,1)

print(our_cache.get(2)) # should be -1


# Test 3: emtpy cache
print('Test 3: ')
our_cache =  LRU_Cache(0)

print(our_cache.get(1)) # should be -1