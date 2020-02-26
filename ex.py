
import os

def find_files_recurse(suffix, path,list_paths):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    for file in os.listdir(path):
      if os.path.isfile(path + '/' + file) and file.endswith(suffix):
        list_paths.append(path+'/' + file)
      elif not os.path.isfile(path+'/' + file):
        find_files_recurse(suffix, path + '/' +file,list_paths)
    return list_paths

def find_files(suffix,path):
  list_paths = []
  return find_files_recurse(suffix, path, list_paths)


# test with testdir
print(find_files('.c','testdir'))
'''
expected result:
['testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/subdir1/a.c', 'testdir/t1.c']
'''

# test present directory for .md
print(find_files('.md', '.'))
'''
expected result:
['./explanation_3.md', './explanation_1.md', './explanation_5.md', './explanation_2.md', './explanation_6.md', './explanation_4.md']
'''

# test whether function works with half the name of the file
print(find_files('_6.md','.'))
'''
expected result:
['./explanation_6.md']
'''