# Blockchain

In this code we are creating a blockchain, which is basically a variant of a LinkedList that maintains a  pointer to the previous node instead of the next. 

## Design

The only requirements of a blockchain is that the first node has value 0 and that the each node maintains a pointer to the previous node. Therefore, we have implemented a variant of linkedin class to abstract the structure of blockchain, with three methods: append, size, and to_list. Also, we have made a new variant of a node that is called a block that contains extra attributes needed for a blockchain, like timestamp.

## Time and Space complexity

The time complexity of each of the three methods (append, size, and to_list) are all O(n), where n is the size of block-chain, since for each method you need to traverse the whole list. The space complexity is also O(n) since you are storing the list (O(n)) and a counter for the size method which is O(1).