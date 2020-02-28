# Analysis of union_intersection
This is an implementation of a standard LinkedList with two additional functions that calculate the union of two lists and another that calculates the intersection
## Design
In order to compute the union and intersection, I have created a helper function that checks whether an element is already in a list. The union function iterates through the first list and appends all the items and then does the same with the other list, while checking if the item is already in the list. The intersection function uses two loops to iterate through each element of the first list and check whether each element is the same as any other element in the other list

## Analysis of time and space complexity

The intersection method  is O(k*n*m) (where n is the length of the first list and m is the length of the second, k is the length of the intersection list) since it uses two loops to iterate both lists and check for common items, as well as a loop to check whether the item is already in the list. The union method is O(n(n+m)) as well since it iterates over each list separately but also checks for whether an item has already been added to the union. The space complexity for the union mehtod is O(n+m) since we maintain at most the sum of the two lists, while the space complexity is O(min(n,m)) since we at most keep the length of smaller list.