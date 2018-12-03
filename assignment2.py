'''
Arvin Aya-ay
CISC320
Programming Assignment 2
'''
import operator

# class to model our output
class contestant:
    def __init__(self, contestantNum, riddlesSolved, riddleTime):
        self.contestantNum = contestantNum
        self.riddlesSolved = riddlesSolved
        self.riddleTime = riddleTime
    def incrementRiddleSolvedCount(self):
        self.riddlesSolved += 1
    def incrementRiddleTime(self, i):
        self.riddleTime += i
    def __str__(self):
        return (str(self.contestantNum) +  " " + str(self.riddlesSolved) +  " " + str(self.riddleTime))
    # defining __lt__ for comparisons between contestants
    def __lt__(self, other):
        if self.riddlesSolved == other.riddlesSolved:
            if self.riddleTime == other.riddleTime:
                return not(self.contestantNum < other.contestantNum)
            else:
                return not(self.riddleTime < other.riddleTime)
        else:
            return self.riddlesSolved < other.riddlesSolved

# dictionary to hold our contestants
contestantDictionary = dict()

# parses a snapshot and adds or modifies contestants in contestantDictionary accordingly
def parseSnapshot(contestantNum, riddleNum, timeOnRiddle, riddleCase):
    # if contestant is already in dictionary adjust values accordingly
    if contestantNum in contestantDictionary:
        c = contestantDictionary[contestantNum]
        if (riddleCase == 'C'):
            c.incrementRiddleSolvedCount()
            c.incrementRiddleTime(int(timeOnRiddle))
        elif (riddleCase == 'I'):
            c.incrementRiddleTime(5)
        # other cases besides 'C' and 'I' do not affect scoring
    # else add a new contestant to the dictionary
    else:
        # init riddles solved and riddle time as 0
        rs = 0
        rt = 0
        if (riddleCase == 'C'):
            rs += 1
            rt += int(timeOnRiddle)
        elif (riddleCase == 'I'):
            rt += 5
        # other cases besides 'C' and 'I' do not affect scoring
        # now add the new contestant to the dictionary
        contestantDictionary[contestantNum] = contestant(contestantNum, rs, rt);

# adding to the contestantDictionary for each line in input
with open('input.txt') as f:
    for line in f:
        a = line.split()
        if a:
            parseSnapshot(a[0], a[1], a[2], a[3])

# write to output file in sorted order
output = open("output.txt", "w")
for key, value in sorted(contestantDictionary.items(), key = lambda x: x[1], reverse = True):
    output.write(str(value) + '\n')
