import re
f = open("day1input.txt", "r")
lines = f.readlines()
calibrationVal = 0
# Part 1
for line in lines:
    search = re.findall(r'\d', line)
    digits = list(map(int, search))
    if(len(search) == 0):
        calibrationAppend = int(search[0])
    else:
        calibrationAppend = int((search[0]) + search[-1])
    print(calibrationAppend)
    calibrationVal += (calibrationAppend)
print(calibrationVal)

# Part 2
calibrationVal = 0
wordToDigits = {'one': 'o1e', 'two': 't2o', 'three': 't3ree', 
                'four': 'f4ur', 'five': 'f5ve', 'six': 's6x', 'seven': 's7ven', 'eight': 'e8ght', 'nine': 'n9ne'}
for line in lines:
    for word in wordToDigits:
        line = line.replace(word, wordToDigits[word]) if word in line else line
    search = re.findall(r'\d', line)
    digits = list(map(int, search))
    calibrationAppend = int((search[0]) + search[-1])
    calibrationVal += (calibrationAppend)
print(calibrationVal)



