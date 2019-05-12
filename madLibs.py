#! python3

# Takes a mad libs text file and finds where an ADJECTIVE, NOUN, ADVERB, VERB should be replaced
# and asks users for a suggestion then saves the suggestion to a text file in the same directory
# Idea from ATBS
# To run type python.exe madLibs.py <path of madlibs text>
# Eg. python.exe C:\Users\Vandy\PycharmProjects\ATBS\madLibs.py C:\Users\Vandy\Desktop\madlibs.txt

import sys, os

if len(sys.argv) == 1:
    print("Please write a madlibs text file path location as the second argument")
elif len(sys.argv) == 2:
    path = sys.argv[1].lower()
    # path = 'C:\\Users\\Vandy\\Desktop\\madlibs.txt'
    if os.path.exists(path):
        madLibsFile = open(path)
        textList = madLibsFile.read().split()
        for word in textList:
            if 'ADJECTIVE' in word.upper():
                index = word.upper().find('ADJECTIVE')
                adjWord = input('Enter an adjective: ')
                textList[textList.index(word)] = word[:index] + adjWord + word[index+9:]
            elif 'NOUN' in word.upper():
                index = word.upper().find('NOUN')
                nounWord = input('Enter a noun: ')
                textList[textList.index(word)] = word[:index] + nounWord + word[index+4:]
            elif 'ADVERB' in word.upper():
                index = word.upper().find('ADVERB')
                advWord = input('Enter an adverb: ')
                textList[textList.index(word)] = word[:index] + advWord + word[index+6:]
            elif 'VERB' in word.upper():
                index = word.upper().find('VERB')
                verbWord = input('Enter a verb: ')
                textList[textList.index(word)] = word[:index] + verbWord + word[index+4:]
        endText = " ".join(textList)
        print(endText)

        endFile = open('%s_filled.txt' % os.path.join(os.path.dirname(path), os.path.basename(path)[:-4]), 'w')
        endFile.write(endText)
        madLibsFile.close()
        endFile.close()


