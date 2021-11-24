from dataclasses import dataclass, field
# python 3.8
from typing import List

# Word
# word: str
# translated_word: str
@dataclass
class Word:
    word: str
    translated_word: str

    def check_translated_word(self, translated_word: str) -> bool:
        assert isinstance(translated_word, str)
        if self.translated_word.lower() == translated_word.lower(): # so soll es sein
            return True
        else:
            return False

@dataclass
class Dictionary:
    language_name: str
    __words: list[Word] = field(default_factory=list) # Python 3.9+

    def add_word(self, word: Word) -> Word:
        assert isinstance(word, Word)
        self.__words.append(word)
        return word
    
    def count_words(self) -> int:
        return len(self.__words)