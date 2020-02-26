# Analysis of Huffman coding solution

Here we implement huffman coding and decoding.

## Design

We start off by creating a huffman node that is similar to a vanilla node with an additional attribute for weight (as well as left,right, value as per normal vanilla node). We then create a function to get frequencies of the individual characters. Also, we create two methods one for creating a huffman tree and another for creating a huffman table. We then create a huffman encoding algorithm and huffman decoding algorithm. The inbuilt method heap

## Time and Space Complexity

Getting the frequencies for the individual characters is O(n) where n is the length of the string/message since you have to traverse each character to count frequencies. Creating the huff tree is O(2^C) where C is the unique characters since you have to recurse on 2 nodes at a time. Creating the huff table is also O(2^C) since you have to traverse the huff tree. Therefore the encoding algorithm is O(2^C) since it consists of using each of the previously mentioned functions to build the solution. For the decoding algorithm the time complexity is O(n*L) Where n is the length of the bit string and the L is the number of Levels in the huff tree since you have to go through each bit character and traverse the tree to get the corresponding character. The space complexity is equivalent to the time complexity since at every step you store what you process.