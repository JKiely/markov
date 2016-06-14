import random

class Ngram:
    def __init__(self, doc):
        self.N = 3
        self.wordlist(doc)
        self.make_db()

    def wordlist(self, doc):
        with open(doc, 'r') as f:
            self.words = f.read().split()

    def grams(self):
        if len(self.words) < self.N:
            raise "Document too short"
        else:
            for i in range(len(self.words) - (self.N-1)):
                chunk = self.words[i:(i+self.N)]
                k = tuple(chunk[:-1])
                v = chunk[-1]
                yield k, v

    def make_db(self):
        self.db = {}
        for k, v in self.grams():
            if k in self.db.keys():
                self.db[k].append(v)
            else:
                self.db[k] = [v]

    def make(self, length=20):
        sentence = list(random.choice(self.db.keys()))
        for _ in xrange(length):
            state = tuple(sentence[-(self.N-1):])
            next_word = random.choice(self.db[state])
            sentence.append(next_word)
        return ' '.join(sentence)
