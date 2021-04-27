"""
Palindrome class realization.
"""

from arraystack import ArrayStack


class Palindrome:
    """
    Class to search palindromes in files.
    """

    def __init__(self):
        pass

    @staticmethod
    def read_file(path: str) -> list:
        """
        Reed file and return list of words from it.
        """
        with open(path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
        words = map(lambda x: x.split()[0], words)
        return words

    @staticmethod
    def write_to_file(word: str, path: str) -> None:
        """
        Write a word to the file.
        """
        with open(path, 'a', encoding='utf-8') as file:
            file.write(word + '\n')

    @staticmethod
    def check(word: str) -> bool:
        """
        Return True if word is a palindrome, False otherwise.
        """
        word_stack = ArrayStack()
        for letter in word:
            word_stack.push(letter)
        reversed_word = ''
        for i in range(len(word_stack)):
            reversed_word += word_stack.pop()
        return word == reversed_word

    def find_palindromes(self, word_file: str, palindrome_file: str) -> list:
        """
        Search for palindromes in word_file and write them into palindrome_file.
        Return list of palindromes.
        """
        words = self.read_file(word_file)
        palindromes = []
        for word in words:
            if self.check(word):
                self.write_to_file(word, palindrome_file)
                palindromes.append(word)
        return palindromes
