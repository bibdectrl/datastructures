from graph import *

def buildGraph(wordlist):
    d = {}
    g = Graph()
    wordfile = open(wordlist, 'r')
    for line in wordfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[1+i:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g
    

wordgraph = buildGraph('american-english')                                
