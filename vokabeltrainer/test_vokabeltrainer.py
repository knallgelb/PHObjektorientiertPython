from vokabeltrainer.classes import Word, Dictionary
import pytest

def test_word():
    word = Word(word="apple", translated_word="Apfel")

    assert word.word == "apple"
    assert word.translated_word == "Apfel"

def test_check_word():
    word = Word(word="apple", translated_word="Apfel")

    assert word.check_translated_word("Apfel") == True
    assert word.check_translated_word("apfel") == True

    assert word.check_translated_word("Einhorn") == False

    with pytest.raises(AssertionError):
        assert word.check_translated_word(["Einhorn"]) == False

    with pytest.raises(AssertionError):
        assert word.check_translated_word(False) == False

def test_dictionary():
    dictionary = Dictionary(language_name="english")

    assert dictionary.language_name == "english"
    assert dictionary.count_words() == 0

def test_dictionary_add_word():
    dictionary = Dictionary(language_name="english")
    word = Word(word="apple", translated_word="Apfel")
    dictionary.add_word(word=word)

    assert dictionary.count_words() == 1
