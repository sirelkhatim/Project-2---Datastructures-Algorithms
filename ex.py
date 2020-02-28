
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

# test when extension is empty
print(find_files('','.'))
'''
expected result:
['./active_directory.py', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir3/subsubdir1/b.h', './testdir/subdir2/.gitkeep', 
'./testdir/subdir4/.gitkeep', './testdir/subdir5/a.h', './testdir/subdir5/a.c', './testdir/subdir1/a.h', './testdir/subdir1/a.c', 
'./testdir/t1.h', './testdir/t1.c', './.git/logs/HEAD', './.git/logs/refs/remotes/origin/master', './.git/logs/refs/heads/master', 
'./.git/objects/39/e842118398c995bfc6d4f6b33997fcf80cfe28', './.git/objects/4a/3e04507c25328fa5a4d1498f37a35f3b4a769b', 
'./.git/objects/ca/da6758a50d58f7a476e5d25719786d306efc1f', './.git/objects/80/2e0ba2aa252ebf4cf4d385fe3395239c6a6e10', 
'./.git/objects/e7/d6d6dca5b7b4e64798fb497bd08f209eb6ed93', './.git/objects/1c/639bb12e6e1325150839ba617304b535b8fd68', 
'./.git/objects/19/91f76a25c7401776e10f037a1a40f83a887d9d', './.git/objects/19/65aac9147958af60df2401e5421f9880b6c69c', 
'./.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391', './.git/objects/12/847bffded5c37ed846023e0c382bdc5c36682d', 
'./.git/objects/e1/bd53e0dd7e816ecf142ad58f02959569aaed9f', './.git/objects/43/fdc5de31fed1116e7367f03f8df56ea80480ec', 
'./.git/objects/dc/d730179ed899e1d2c356fb49efcccb3637ecb9', './.git/objects/f2/94d609436692fbfd8eced4386c5efbc2788029', 
'./.git/objects/d0/53cd74d1ed2c242b3bb800c184e7166e7dba74', './.git/objects/06/1499b6de188986d25444c8e6c6970cef7769a5', 
'./.git/objects/6a/1734955efa1eac5de17ea02f8238877d34de58', './.git/objects/1b/e32ef99aca26cafdc0b1a19ae57b1b170dbd70', 
'./.git/objects/b6/8eaf01e7359a7a90ada0e43c40b40f978a51a7', './.git/objects/b6/1411a89911f0e79dd4600441273499abdc8574', 
'./.git/objects/8e/6cd5e84b52a0bbf7f78fd4ee7ffb1feda8d616', './.git/objects/de/fb6130ecd8f6bbda6d2db990e5897fb09041fb', 
'./.git/objects/fd/8218220817e77934febab300466756d165ec12', './.git/objects/c6/c1fd1bebe099660d0af3818f9cc2a36aaa4a21', 
'./.git/objects/1d/7d684dfa4069f4f8b32e78290805a7bd67d500', './.git/objects/9f/246f9d4b7b426a875d3aaea180212aed82b2fb', 
'./.git/objects/1a/fb26720ab193014c48e177f8fc3c1a7ae7fe5e', './.git/objects/54/f0ec69ea93744e2820ffc5eb4ac5707c9d2513', 
'./.git/objects/d5/64d0bc3dd917926892c55e3706cc116d5b165e', './.git/hooks/post-update.sample', './.git/hooks/pre-receive.sample', 
'./.git/hooks/pre-push.sample', './.git/hooks/commit-msg.sample', './.git/hooks/update.sample', './.git/hooks/pre-commit.sample', 
'./.git/hooks/fsmonitor-watchman.sample', './.git/hooks/pre-applypatch.sample', './.git/hooks/pre-rebase.sample', './.git/hooks/prepare-commit-msg.sample', 
'./.git/hooks/applypatch-msg.sample', './.git/config', './.git/index', './.git/HEAD', './.git/info/exclude', './.git/refs/remotes/origin/master', 
'./.git/refs/heads/master', './.git/description', './.git/COMMIT_EDITMSG', './explanation_3.md', './blockchain.py', './explanation_1.md', './explanation_5.md', 
'./explanation_2.md', './ex.py', './explanation_6.md', './explanation_4.md', './union_intersection.py', './huffman.py', './lru_cache.py']

'''
#test case when extension is a folder name
print(find_files('', 'testdir'))
'''
expected result: 
['testdir/subdir3/subsubdir1/b.c', 'testdir/subdir3/subsubdir1/b.h', 
'testdir/subdir2/.gitkeep', 'testdir/subdir4/.gitkeep', 'testdir/subdir5/a.h', 
'testdir/subdir5/a.c', 'testdir/subdir1/a.h', 'testdir/subdir1/a.c', 'testdir/t1.h', 
'testdir/t1.c']
