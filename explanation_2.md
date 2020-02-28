# Analysis for Finding files

This is a recursive algorithm that traverses a folder and recurses on the subfolders to find a certain file.

## Design
This is a classic recursive algorithm that makes use of a recursive base algorithm find_files_recurse which is called within the main function files_recurse.

## Time and Space Complexity

The time complexity is exponential O(d*w) where d is the depth of the folder tree and w is the number of children since the algorithm is a recursive one, it uses a call stack which is effectively like a depth first search tree. The space complexity is O(1), since no value is being stores as such.
