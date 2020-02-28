# Analysis of active directory

This solution attempts to check whether a user is in a group. The trick here is to be able to recurse within a group to find a user even if there is a group within a group.

## Design
This is a recursive function that first checks whether the user is within the group if not, it iterates through every group and recurses through each group to find the user.

## Analysis of time and space complexity
The space complexity is O(nG + nU) where nG is the number of groups and nU is the number of users, since you end up with lists that are equivalent to the size of the users (group.get_users) and (group.get_groups()). The time complexity is quadractic (O(nm)) where m is the number of users and n is the number of groups, since we use recursion, which essentially uses a call stack that is similar to a depth first search tree.

