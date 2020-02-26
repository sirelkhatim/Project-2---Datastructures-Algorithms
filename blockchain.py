import hashlib
import datetime


def calc_hash(data):

    sha = hashlib.sha256()
    encoded_str = data.encode('utf-8')
    sha.update(encoded_str)

    return sha.hexdigest()

class Block:

    def __init__(self,  data, previous_hash):
        self.timestamp = datetime.datetime.utcnow()
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = calc_hash(data)


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
