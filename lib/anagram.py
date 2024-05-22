# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        sorted_word = sorted(self.word)
        for anagram in possible_anagrams:
            if self._is_anagram(anagram.lower(), sorted_word):
                matches.append(anagram)
        return matches

    def _is_anagram(self, candidate, sorted_word):
        if candidate == self.word:
            return False
        return sorted(candidate) == sorted_word
