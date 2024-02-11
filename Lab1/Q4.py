from random import choices


class TextGenerator:
    def __init__(self):
        self.prefixDict = {}

    def assimilateText(self, filename):
        self.prefixDict.clear()

        with open(filename, 'r') as file:
            inputText = file.read()

        words = inputText.split()

        if len(words) < 3:
            raise ValueError("Number of words in text file is less than 3.")

        word1, word2 = words[0], words[1]

        for i in range(2, len(words)):
            currWord = words[i]
            currTuple = (word1, word2)

            if currTuple not in self.prefixDict:
                self.prefixDict[currTuple] = []
            self.prefixDict[currTuple].append(currWord)

            word1 = word2
            word2 = currWord

    def generateText(self, n, startWord=''):
        tuples = list(self.prefixDict.keys())

        if startWord:
            startTuples = [t for t in tuples if t[0] == startWord]
            if not startTuples:
                raise ValueError('Unable to produce text with the specified start word.')
            currTuple = choices(startTuples)[0]
        else:
            currTuple = choices(tuples)[0]

        text = currTuple[0] + " " + currTuple[1] + " "
        wordCount = 2

        while wordCount < n:
            if currTuple in self.prefixDict:
                newWord = choices(self.prefixDict[currTuple])[0]
                text += newWord + " "
                currTuple = (currTuple[1], newWord)
                wordCount += 1
            else:
                currTuple = choices(tuples)[0]

        print(text)


def main():
    gen = TextGenerator()
    gen.assimilateText("sherlock.txt")

    with open("prefixes.txt", "w") as f:
        f.write(str(gen.prefixDict))

    gen.generateText(100, startWord='London')


if __name__ == "__main__":
    main()
