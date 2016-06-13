import random

class Bigram:
    def __init__(self, doc):
        self.wordlist(doc)
        self.make_grams()

    def wordlist(self, doc):
        with open(doc, 'r') as f:
            self.words = f.read().split()

    def make_grams(self):
        if len(self.words) < 2:
            return
        self.grams = {}
        for i in range(len(self.words) - 1):
            word = self.words[i]
            follower = self.words[i+1]
            if word in self.grams.keys():
                self.grams[word].append(follower)
            else:
                self.grams[word] = [follower]

    def make(self, length=20):
        start = random.randint(0, (len(self.words) - 1))
        start_word = self.words[start]
        sentence = [start_word]
        for _ in range(length):
            last_word = sentence[-1]
            next_word = random.choice(self.grams[last_word])
            sentence.append(next_word)
        return ' '.join(sentence)
