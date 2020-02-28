class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if not isinstance(group, Group):
        return "group entered is not an instance of the Group Class"
    if user is None:
        return "No user to look for!"
    in_group = user in group.get_users()
    if in_group:
        return True

    # iterate through groups to check if 
    for grp in group.get_groups():
        if is_user_in_group(user, grp):
            return True
    
    return False


# Test 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print('Test 1: (2 nested groups in a group) ')
print(is_user_in_group(sub_child_user, child)) # should be True

# Test 2: Trivial
print('Trivial test: ')
trivial= Group('trivial')
print(is_user_in_group('hassan',parent)) # should be False


group1 = Group("tree")
group2 = Group("sub-tree")
group3 = Group("sub_tree 2")
group4 = Group("sub-sub tree")

group1.add_group(group2)
group1.add_group(group3)
group3.add_group(group1)
group3.add_user('hassan')
group4.add_user('Noon')
group1.add_user('Mom')

print("Cyclical group structure test: ")

print(is_user_in_group('Noon', group4)) # should be True
print("Cyclical group structure test2: ")
print(is_user_in_group('Mom', group3)) # should be True

print("Cyclical group structure test3: ")
print(is_user_in_group('Mom', group2)) # should be False

## Test 3: Passing in  no user as an argument
print(is_user_in_group(user =None, group = group1))

'''
expected result:
No user to look for!
'''

# Test 4: Passing is a argument to group that isn't a group
print(is_user_in_group('sub_child_user', sub_child_user))

'''
expected result:
group entered is not an instance of the Group Class
'''