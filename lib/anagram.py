# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
    def match(self, list):
        matches= []
        for word in list:
            if sorted([letter for letter in word]) == self.word_letters:
                matches.append(word)
        return matches

   
        