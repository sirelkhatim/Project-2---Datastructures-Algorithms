# Analysis for Finding files

This is a recursive algorithm that traverses a folder and recurses on the subfolders to find a certain file.

## Design
This is a classic recursive algorithm that makes use of a recursive base algorithm find_files_recurse which is called within the main function files_recurse.

## Time and Space Complexity

The time complexity is exponential O(2^n) where n is the largest number of files in a subdirectory. The space is complexity is O(1), since no value is being stores as such.
