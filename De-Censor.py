'''
I have it reading a list of swear words from a file called "swear.txt", 
and reading the actual text from a file called "text.txt"

@author: Sam
'''
import sys

class decensorer:
    
    def __init__(self, listOfWords):
        self.listOfWords = listOfWords
        
    def uncensor(self, word):
		word = word.strip()
		for swear in listOfWords: 
			swear = swear.strip()
			if word[0] == swear[0] and len(word) == len(swear):
				return swear
		return word

sys.stdin = open('text.txt')

input = sys.stdin

output = ""

listOfWords = []

for word in open('swear.txt').read().split(" "):
	listOfWords.append(word)

d = decensorer(listOfWords)
for line in input:
    for word in line.split(' '):
        if "*" in word:
			output += d.uncensor(word) + " "
        else:
            output += word + " "

print output
