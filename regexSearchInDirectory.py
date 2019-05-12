#! python3

# Searches for all occurrences regex expression in the files of a directory
# Idea from ATBS
# To run type python.exe regexSearchInDirectory.py <regex expression> <directory path>
# Eg. python.exe C:\Users\Vandy\PycharmProjects\ATBS\regexSearchInDirectory.py '\d+-\d+' C:\Users\Vandy\PycharmProjects\ATBS\RegexSearchDir

import re, sys, os

if len(sys.argv) != 3:
    print("Please write a regex expression as the second argument in single quotes and a directory path for the third argument")
elif not os.path.isdir(sys.argv[2]):
    print("That is an invalid directory")
else:
    regex = re.compile(sys.argv[1][1:-1])
    path = sys.argv[2].lower()
    # regex = re.compile(r'\d+-\d+')
    # path = r'C:\Users\Vandy\Desktop\Regex Search Test'
    for filename in os.listdir(path):
        file = open(os.path.join(path, filename))
        # Should come up with better way to find line number
        i = 1
        for line in file.readlines():
            for entry in regex.findall(line):
                print(f"Found '{entry.rstrip()}' at Line {i} in {filename}")
            i += 1
        file.close()