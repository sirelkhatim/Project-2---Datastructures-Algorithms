import hashlib
import datetime


def calc_hash(data, timestamp, previous_hash):

    sha = hashlib.sha256()
    encoded_str = f'{timestamp}\n{data}\n{previous_hash}'.encode('utf-8')
    sha.update(encoded_str)

    return sha.hexdigest()

class Block:

    def __init__(self,  data, previous_hash):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = calc_hash(data, self.timestamp, previous_hash)


    def __str__(self):
        return str(self.timestamp) + " " + str(self.data) + " " + str(self.previous_hash) + " " + str(self.hash)


class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Block(data, 0)
            return

        new_head = Block(data, self.head.hash)
        new_head.previous_block = self.head
        self.head = new_head

    def size(self):
        if self.head is None:
            return 0
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.previous_block
        return count

    def to_list(self):
        list_output = []
        node = self.head
        while node:
            list_output.append(node)
            node = node.previous_block

        return list_output




"""
**************  End of Program  *****************
"""    


#Testing code
"""
Test Case 1
"""
print("Test Case 1: Empty BlockChain")
A = BlockChain()
print("size",A.size())
print(A.head)
print()

'''
expected result:
size 0
None
'''

"""
Test Case 2
"""
print("Test Case 2: 1 block")
B = BlockChain()
B.append("Genesis")
print("size",B.size())
for item in B.to_list():
    print(item)
print()

'''
expected result:
size 1
2020-02-27 23:47:11.033108 Genesis 0 1ddf226ac471cb1a30f70cc02596747d3a4631a41111b1ce6f8b0ccd3b00d844
'''

"""
Test Case 3
"""
print("Test Case 3: More than one block")
D = BlockChain()
D.append("Lol")
D.append("We are together")
D.append("Time again")
D.append("The alphabet")
D.append("Once you go, you really go")

print("size",D.size())
for item in D.to_list():
    print(item)
'''
expected result:
size 5
2020-02-27 23:47:11.033176 Once you go, you really go a52bf0a349124bd1b14be7ab1036e9bb8f3b15e39996c739d5f7e6bdb2b80493 53598d7223278e768460bdcfe10983db2b95b729f23749ab43a51d68e5e4768c
2020-02-27 23:47:11.033172 The alphabet 0b41aeca9b8567539e897d67c4720c1de901bc91d9835200e40af2d063c44148 a52bf0a349124bd1b14be7ab1036e9bb8f3b15e39996c739d5f7e6bdb2b80493
2020-02-27 23:47:11.033167 Time again d39e04f49bf4944a47ebca1f87e7cc2591b210952c60e4bf8eb786cc0c407886 0b41aeca9b8567539e897d67c4720c1de901bc91d9835200e40af2d063c44148
2020-02-27 23:47:11.033162 We are together 4c48ddca009b7afb3e20c84628477eaf10d56233ae8b2923acff5213af097dbe d39e04f49bf4944a47ebca1f87e7cc2591b210952c60e4bf8eb786cc0c407886
2020-02-27 23:47:11.033154 Lol 0 4c48ddca009b7afb3e20c84628477eaf10d56233ae8b2923acff5213af097dbe
'''

"""
Test Case 4
"""
print("Test Case 4: Appending empty data")
E = BlockChain()
E.append("")


print("size",E.size())
for item in E.to_list():
    print(item)

"""
expected result:
size 1
2020-02-27 23:52:03.369625  0 edd0549380b370cffa56240cc7bd2e6654914925bbaa50377af0992c4815d478
"""