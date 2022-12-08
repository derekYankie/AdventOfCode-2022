'''
The total sizes of the directories above can be found as follows...
The total size of directory e is 584 because it contains a single file i of size 584 and no other directories.  
The directory a has total size 94853 because it contains files f (size 29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a contains e which contains i).
Directory d has total size 24933642.
As the outermost directory, / contains every file. Its total size is 48381165, the sum of the size of every file.
'''
import re
with open("puzzle-input-07","r") as file:
    input = file.read().strip().split('\n')

# Recursive function for exploring directories
def search_directory(line_index):
    i=line_index
    directory_size=0
    while i < len(input):
        if len(re.findall(r'\d+',input[i]))!=0: directory_size+=int(re.findall(r'\d+',input[i])[0])
        if 'cd ..' in input[i]:
            directories_sizes.append(directory_size)
            return directory_size,i
        if '$ cd' in input[i]:
            subdirectory_size,i=search_directory(i+1)
            directory_size+=subdirectory_size            
        i+=1

    directories_sizes.append(directory_size)   
    return directory_size,i


directories_sizes = []
# print(search_directory(1)) # (44795677, 1010)
search_directory(1)

total_size = 0
for size in directories_sizes:
    if size<=100000:
        total_size+=size

print("Total size of all directories under 100000 size:",total_size)

# Part Two
directories_sizes = []
search_directory(2)

disk_space = 70000000-directories_sizes[-1]
possible_directories = []
for size in directories_sizes:
    if disk_space+size >= 30000000:
        possible_directories.append(size)

print("Size of smallest directory to delete:",min(possible_directories))
