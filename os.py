import os


print(os.listdir())
print(os.getcwd())

for dirpath, dirnames, filenames in os.walk('Users/etismeimet/Desktop'):
    print('current path:', dirpath)
    print('directories:', dirnames)
    print('files:', filenames)
    print()

print(dir(os.path))
