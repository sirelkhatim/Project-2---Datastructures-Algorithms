# Analysis of active directory

This solution attempts to check whether a user is in a group. The trick here is to be able to recurse within a group to find a user even if there is a group within a group.

## Design
This is a recursive function that first checks whether the user is within the group if not, it iterates through every group and recurses through each group to find the user.

## Analysis of time and space complexity
The space complexity is O(1) since we don't maintain storage in the recursion. The time complexity is exponential (O(2^m)) where m is the maximum number of leaves of all the levels.

