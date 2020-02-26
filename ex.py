
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